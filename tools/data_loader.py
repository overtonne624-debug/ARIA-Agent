import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }