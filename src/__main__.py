from .json_loader import load_json, get_parameters
from .generator import Generator
from .parser import extract_arguments
from .json_builder import build_json, write_json
from .validator import validator


prompt = load_json("data/input/function_calling_tests.json")
functions = load_json("data/input/functions_definition.json")

test = Generator()
result = []
for prom in prompt:
    function_name = test.generate(prom["prompt"], functions, 20)

    parameters = get_parameters(function_name, functions)

    if parameters is None:
        continue

    argument = extract_arguments(prom["prompt"], parameters)

    if validator(argument, parameters):
        json_extratcted = build_json(
            prom["prompt"],
            function_name,
            argument
        )
        result.append(json_extratcted)

write_json(result, "data/output/function_calling_results.json")
print(result)