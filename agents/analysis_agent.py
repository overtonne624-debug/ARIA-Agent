import shap
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, r2_score
from xgboost import XGBClassifier
from xgboost import XGBRegressor


def run_analysis(df, target_column):

    df = df.copy()

    drop_cols = [
        "Student_Names",
        "Phone_No.",
        "Phone No.",
        "Name",
        "Email",
        "Comment",
        "CourseCode",
        "ListofCourses"
    ]

    for col in drop_cols:
        if col in df.columns:
            df = df.drop(columns=[col])

    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Remove empty targets
    mask = y.notna()
    X = X[mask]
    y = y[mask]

    # Encode ALL columns that contain strings (not just object dtype)
    for col in X.columns:
        if X[col].dtype == "object" or X[col].apply(lambda v: isinstance(v, str)).any():
            X[col] = LabelEncoder().fit_transform(X[col].astype(str))

    X = X.fillna(0)

    # Force X to numeric, coerce any remaining stragglers
    X = X.apply(pd.to_numeric, errors="coerce").fillna(0)

    # Detect classification
    is_classification = (
        y.dtype == "object"
        or y.nunique() <= 20
    )

    # Encode y BEFORE the split
    if is_classification:
        y = LabelEncoder().fit_transform(y.astype(str))
    else:
        y = pd.to_numeric(y, errors="coerce").fillna(0).values

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    if is_classification:
        models = {
            "RandomForest": RandomForestClassifier(random_state=42),
            "LogisticRegression": LogisticRegression(
                max_iter=5000,
                solver="lbfgs"
            ),
            "XGBoost": XGBClassifier(
                eval_metric="logloss",
                random_state=42
            )
        }

        best_model = None
        best_score = 0
        best_model_object = None

        for name, model in models.items():
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            score = accuracy_score(y_test, predictions)

            if score > best_score:
                best_score = score
                best_model = name
                best_model_object = model

        explainer = shap.TreeExplainer(best_model_object)
        shap_values = explainer.shap_values(X_test)

        if isinstance(shap_values, list):
            shap_values = shap_values[0]

        importance = np.abs(shap_values).mean(axis=0)

        if len(importance.shape) > 1:
            importance = importance.mean(axis=1)

        feature_importance = {}

        for col, imp in zip(X.columns, importance):
            feature_importance[str(col)] = float(imp)

        feature_importance = dict(
            sorted(
                feature_importance.items(),
                key=lambda item: float(item[1]),
                reverse=True
            )[:5]
        )

        feature_importance = {
            str(k): float(v)
            for k, v in feature_importance.items()
        }

        print("CLASSIFICATION X SHAPE:", X.shape)
        print("CLASSIFICATION X COLUMNS:", list(X.columns))

        return {
            "problem_type": "classification",
            "best_model": str(best_model),
            "score": float(round(best_score, 4)),
            "top_features": feature_importance,
            "model_object": best_model_object,
            "feature_names": list(X.columns),
            "processed_X":X,
            "processed_X_shape": list(X.shape)
        }

    else:
        models = {
            "RandomForest": RandomForestRegressor(random_state=42),
            "XGBoost": XGBRegressor(random_state=42)
        }

        best_model = None
        best_score = -999
        best_model_object = None

        for name, model in models.items():
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            score = r2_score(y_test, predictions)

            if score > best_score:
                best_score = score
                best_model = name
                best_model_object = model

        print("REGRESSION X SHAPE:", X.shape)
        print("REGRESSION X COLUMNS:", list(X.columns))

        return {
            "problem_type": "regression",
            "best_model": best_model,
            "score": round(best_score, 4),
            "feature_names": list(X.columns),
            "model_object": best_model_object,
            "processed_X":X,
            "processed_X_shape":list(X.shape)
        }