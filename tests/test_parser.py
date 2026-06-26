from ..src.json_loader import load_functions, load_tests, build_prompt

functions = load_functions(
    "data/input/functions_definition.json"
)

tests = load_tests(
    "data/input/function_calling_tests.json"
)

# print(functions)
# print("----------------")
# print(tests)


# functions = load_functions(...)

prompt = build_prompt(
    functions,
    "What is the sum of 2 and 3?"
)

print(prompt)