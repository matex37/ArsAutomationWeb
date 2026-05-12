import json
from pathlib import Path
from faker import Faker

fake = Faker("en_CA")


def replace_faker(data):

    if isinstance(data, dict):
        return {
            key: replace_faker(value)
            for key, value in data.items()
        }

    elif isinstance(data, list):
        return [
            replace_faker(item)
            for item in data
        ]

    elif isinstance(data, str):

        faker_map = {
            "{{first_name}}": fake.first_name(),
            "{{last_name}}": fake.last_name(),
            "{{email}}": fake.email(),
            "{{street_address}}": fake.street_address(),
            "{{phone_number}}": fake.phone_number(),
            "{{company}}": fake.company()

        }

        return faker_map.get(data, data)

    return data


def load_booking_data():

    path = (
        Path(__file__).parent.parent
        / "booking_data.json"
    )

    with open(path, "r", encoding="utf-8") as f:

        data = json.load(f)

    return replace_faker(data)