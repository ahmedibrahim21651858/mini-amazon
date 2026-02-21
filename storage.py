import json
import os

def load_data(filename, default):
    if not os.path.exists(filename):
        save_data(filename, default)
        return default

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return default


def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
