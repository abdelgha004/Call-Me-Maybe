import json 

def load_functions(path):
    try:

        with open(path)as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON file: {path}")
        return []


def load_tests(path):
    try:

        with open(path)as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON file: {path}")
        return []
