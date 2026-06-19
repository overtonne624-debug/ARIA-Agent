import pandas as pd


def run_critic(df, target_column):

    warnings = []

    # Missing values
    missing_pct = (
        df.isnull().sum().sum()
        / (df.shape[0] * df.shape[1])
    )

    if missing_pct > 0.1:
        warnings.append(
            "High missing value percentage detected"
        )

    # Class imbalance
    if target_column in df.columns:

        counts = (
            df[target_column]
            .value_counts(normalize=True)
        )

        if counts.max() > 0.8:
            warnings.append(
                "Potential class imbalance"
            )

    confidence = max(
        0.5,
        1 - (0.1 * len(warnings))
    )

    return {
        "confidence": round(confidence, 2),
        "warnings": warnings
    }