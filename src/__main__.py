from .parser import load_json

functions = load_json("data/input/function_definitions.json")
tests = load_json("data/input/function_calling_tests.json")

result = []

for test in tests:
    valuo = test["prompt"]

    item = {}
    item["prompt"] = valuo
    item["name"] = ""
    item["parameters"] = {}
    result.append(item)


print(result)