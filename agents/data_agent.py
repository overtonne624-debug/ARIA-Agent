import pandas as pd

def analyze_dataset(df):

    preferred_targets = [
        "Grade",
        "Course_Recommendation",
        "RatingOfCourses"
    ]

    possible_target = None

    for col in preferred_targets:
        if col in df.columns:
            possible_target = col
            break

    if possible_target is None:
        possible_target = df.columns[-1]

    if pd.api.types.is_numeric_dtype(df[possible_target]):
        unique_values = df[possible_target].nunique()

        if unique_values <= 10:
            problem_type = "classification"
        else:
            problem_type = "regression"
    else:
        problem_type = "classification"

    return {
        "possible_target": possible_target,
        "problem_type": problem_type,
        "rows": df.shape[0],
        "columns": df.shape[1]
    }