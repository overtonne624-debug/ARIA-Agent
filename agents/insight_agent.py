def generate_insights(df):
    insights = []

    insights.append(
        f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns."
    )

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:
        insights.append(
            f"{col}: Average = {round(df[col].mean(), 2)}"
        )

    return insights