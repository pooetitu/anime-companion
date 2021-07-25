import json
from pathlib import Path


def load_view_list_data():
    file = Path("./assets/animes.json")
    if file.exists():
        with open("./assets/animes.json", "r") as file:
            data = json.load(file)
            return data
    data = {}
    return data


def save_view_list_data(anime_list):
    with open("./assets/animes.json", "w") as file:
        file.write(json.dumps(anime_list, sort_keys=True, indent=4))
