import pandas as pd
from pathlib import Path

def transform_data(input_path="data/bronze/breweries_raw.csv", output_path="data/silver/breweries.parquet"):
    df = pd.read_csv(input_path)
    df = df.dropna(subset=["state", "brewery_type"])
    df["state"] = df["state"].str.upper()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Transformado para: {output_path}")
