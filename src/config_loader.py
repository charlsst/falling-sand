from pathlib import Path
import json

def load_config():
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"

    if not config_path.exists():
        raise FileNotFoundError("config.json not found")

    with open(config_path) as f:
        return json.load(f)