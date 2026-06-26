from .generator import Generator
from .parser import build_prompt
from .json_loader import load_json


functions = load_json(
    "data/input/functions_definition.json"
)

generator = Generator()


# prompt = build_prompt(
#     functions,
#     "What is the sum of 2 and 3?"
# )
prompt = "Choose function: fn_add_numbers or fn_greet. Answer:"
# prompt = build_prompt(
#     functions,
#     "Greet john"
# )

result = generator.generate(
    prompt,
    functions,
    max_tokens=10
)


print("Generated function:")
print(result)