import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


PW = get_secret("PW")
PW_CERT = get_secret("PW_CERT")
TOKEN = get_secret("TOKEN")
ID = get_secret("ID")

if __name__ == "__main__":

    
    print("연결")