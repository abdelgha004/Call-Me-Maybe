from llm_sdk import Small_LLM_Model
from .json_loader import load_json

model = Small_LLM_Model()
functions = load_json(
    "data/input/functions_definition.json"
)


for func in functions:
    name = func["name"]
    token = model.encode(name)
    ids = token[0].tolist()
    print(f"{name}: {ids}\n")
