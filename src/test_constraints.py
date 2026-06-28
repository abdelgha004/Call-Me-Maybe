from src.constraints import Constraints

functions = [
    {"name": "fn_add_numbers"},
    {"name": "fn_greet"},
]

constraints = Constraints()

function_tokens = constraints.build_function_tokens(functions)

print(function_tokens)
print()

print("Case 1:")
print(constraints.get_allowed_tokens(function_tokens, []))

print()

print("Case 2:")
print(constraints.get_allowed_tokens(function_tokens, [8822]))

print()

print("Case 3:")
print(constraints.get_allowed_tokens(function_tokens, [8822, 2891]))

print()

print("Case 4:")
print(constraints.get_allowed_tokens(function_tokens, [8822, 1889]))