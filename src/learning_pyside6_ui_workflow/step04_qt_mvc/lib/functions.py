import json
from pathlib import Path
from typing import Any

DIR_FILE = Path(__file__).parent
DIR_DATA = DIR_FILE.with_name("data")

def print_text(value: Any):
    print(value)


def load_json_data() -> list[Any]:
    items = []
    for path in DIR_DATA.glob("*.json"):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            items.append(data)
    return items
