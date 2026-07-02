
from .json_loader import load_json, get_parameters
from .generator import Generator

from .json_builder import build_json, write_json

# removed
# from .parser import extract_arguments
# from .validator import validator

from .cli import parse_arguments

args = parse_arguments()

prompt = load_json(args.input)
functions = load_json(args.functions_definition)

test = Generator()

# result = [] removed

for prom in prompt:
    function_name = test.generate(prom["prompt"], functions, 20)

    parameters = get_parameters(function_name, functions)

    if parameters is None:
        continue

    # argument = 

# removed
    # if validator(argument, parameters):
    #     json_extratcted = build_json(
    #         prom["prompt"],
    #         function_name,
    #         argument
    #     )
    #     result.append(json_extratcted)
# ------------------
# removed
# write_json(result, args.output)
# print(result)
# ----------------------