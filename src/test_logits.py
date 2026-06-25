from llm_sdk import Small_LLM_Model



model = Small_LLM_Model()

text = "The sum of 2 and 3 is "

tokens = model.encode(text)

print(tokens)
ids = tokens[0].tolist()

logist = model.get_logits_from_input_ids(ids)
print("-------------------")

print(len(logist))
print(type(logist))
print("-------------------")

print(logist[:10])
print("-------------------")

max_scor = max(logist)
print(max_scor)
print("-------------------")

index = logist.index(max_scor)
print(index)
print("-------------------")

next_token = model.decode(index)
print(next_token)
print("-------------------")


top_tokens = sorted(enumerate(logist), key=lambda x: x[1], reverse=True)[:5]

for id, score in top_tokens:
    token = model.decode(id)
    
    print(id, score, token)

print("-------------------")

def generate(prompt, max_tokens):
    result = prompt

    for _ in range(max_tokens):
        top_key_prediction = get_top_k_predictions(result, 5)
        next_id = choose_token(top_key_prediction)
        next_token = model.decode(next_id)
        result += next_token
    return result


def get_top_k_predictions(prompt, k):
    tokens = model.encode(prompt)
    ids = tokens[0].tolist()
    logits = model.get_logits_from_input_ids(ids)
    top_k = sorted(enumerate(logits), key=lambda x: x[1], reverse=True)[:k]
    prediction = []
    for id , score in top_k:
        token = model.decode(id)
        prediction.append((id, token, score))
    return prediction


def choose_token(top_k_predictions):
    token = top_k_predictions[0][0]
    return token


print(generate("The sum of 2 and 3 is", 5))

print(generate("The capital of France is", 10))
print(generate("The sum of 2 and 3 is", 10))
