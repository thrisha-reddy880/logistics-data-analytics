from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "outputs"

DATA_FILE = DATA_DIR / "DataCoSupplyChainDataset.csv"

OUTPUT_DIR.mkdir(exist_ok=True)
