import json
from pathlib import Path

from src.status_enum import ViewStatus


def load_view_list_data():
    file = Path("./assets/animes.json")
    if file.exists():
        with open("./assets/animes.json", "r") as file:
            data = json.load(file)
            return data
    else:
        data = {}
        return data


def save_view_list_data(anime_list):
    with open("./assets/animes.json", "w") as file:
        file.write(json.dumps(anime_list, default=str, sort_keys=True, indent=4, cls=EnumEncoder))

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) in ViewStatus.values():
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)

def as_enum(d):
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        return getattr(ViewStatus[name], member)
    else:
        return d