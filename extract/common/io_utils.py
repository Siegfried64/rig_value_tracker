from datetime import datetime
from pathlib import Path
import pyarrow.parquet as pq

def generate_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")

def create_path(base_dir, source_name, timestamp):
    path = Path(base_dir) / source_name
    path.mkdir(parents=True, exist_ok=True)
    return path / f"{timestamp}.parquet"

def write_parquet(table, path):
    pq.write_table(table, path)

