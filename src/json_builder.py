import json

def build_json(prompt, function_name, arguments):
    result = {}
    result["prompt"] = prompt
    result["name"] = function_name
    result["parameters"] = arguments
    return result

def write_json(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)