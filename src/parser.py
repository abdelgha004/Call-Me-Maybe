import json


def load_json(path: str):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data

    except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")

    except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {path}")

    except Exception as e:
        raise ValueError(f"Error loading {path}: {e}")
