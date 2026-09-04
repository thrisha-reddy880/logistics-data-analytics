import pandas as pd
from .config import DATA_FILE

def load_data(path=DATA_FILE):
    """Load the DataCo supply-chain CSV."""
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. "
            "Download DataCoSupplyChainDataset.csv and place it in data/."
        )

    return pd.read_csv(path, encoding="latin1")

def profile_data(df):
    """Return basic data-quality information."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": df.isna().sum().sort_values(ascending=False)
    }
