import os
import shap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_feature_importance(model, feature_names):

    if not hasattr(model, "feature_importances_"):
        return {}

    importance = model.feature_importances_

    result = {}

    for feature, score in zip(feature_names, importance):
        result[feature] = round(float(score * 100), 2)

    result = dict(
        sorted(
            result.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    return result


def generate_shap_explanation(model, X):

    try:
        print("========== SHAP DEBUG ==========")
        print("TYPE:", type(X))

        if hasattr(X, "shape"):
            print("SHAPE:", X.shape)

        print("COLUMNS:")
        print(X.columns)

        print("HEAD:")
        print(X.head())

        print("================================")

        os.makedirs("reports", exist_ok=True)

        if isinstance(X, list):
            X = pd.DataFrame(X)

        if len(X) > 200:
            X = X.head(200)

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(X)

        print("SHAP TYPE:", type(shap_values))
        print("SHAP SHAPE:", np.array(shap_values).shape)

        if isinstance(shap_values, list):
            shap_values = shap_values[0]

        elif len(np.array(shap_values).shape) == 3:
            shap_values = shap_values[:, :, 0]

        shap.summary_plot(
            shap_values,
            X,
            show=False
        )

        plt.tight_layout()

        output_path = "reports/shap_summary.png"

        plt.savefig(output_path)

        plt.close()

        return output_path

    except Exception as e:
        print("===================================")
        print("SHAP ERROR")
        print(str(e))
        print("===================================")

        raise


def generate_explanation(feature_importance):

    if not feature_importance:
        return {
            "most_important_feature": "Unknown",
            "reason": "No feature importance available"
        }

    top_feature = list(feature_importance.keys())[0]

    return {
        "most_important_feature": top_feature,
        "reason": f"{top_feature} contributed most to the model prediction"
    }