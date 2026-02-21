import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    # Normalize column names (CRITICAL)
    df.columns = [c.strip().lower() for c in df.columns]

    print("Detected columns:", list(df.columns))
    return df