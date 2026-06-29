import json 

def load_json(path):
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

def get_parameters(function_name, functions):
    for func in functions:
        if func["name"] == function_name:
            return func["parameters"]