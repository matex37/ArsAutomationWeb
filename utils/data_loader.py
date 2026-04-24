import json
from pathlib import Path


def load_booking_data():
    path = Path(__file__).parent.parent /"booking_data.json"

    with open(path, "r") as f:
        return json.load(f)