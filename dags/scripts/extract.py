import requests
import pandas as pd
from pathlib import Path

def fetch_breweries(api_url="https://api.openbrewerydb.org/breweries", save_path="data/bronze/breweries_raw.csv"):
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"Salvo: {save_path}")

if __name__ == "__main__":
    fetch_breweries()
