from llm_sdk import Small_LLM_Model

model = Small_LLM_Model()



prompt = "Hello"

tokens = model.encode(prompt)

ids = tokens[0].tolist()
logits = model.get_logits_from_input_ids(ids)
print(len(logits))
