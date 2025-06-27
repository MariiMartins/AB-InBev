import pandas as pd
from scripts.extract import fetch_breweries

def test_fetch_breweries(tmp_path):
    out_file = tmp_path / "breweries.csv"
    fetch_breweries(save_path=out_file)
    df = pd.read_csv(out_file)
    assert not df.empty
    assert "name" in df.columns
