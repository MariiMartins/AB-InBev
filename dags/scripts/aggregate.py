import pandas as pd
from pathlib import Path

def aggregate_data(input_path="data/silver/breweries.parquet", output_path="data/gold/brewery_summary.csv"):
    df = pd.read_parquet(input_path)
    agg = df.groupby(["state", "brewery_type"]).size().reset_index(name="brewery_count")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    agg.to_csv(output_path, index=False)
    print(f"Agregado em: {output_path}")
