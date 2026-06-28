

def extract_arguments(user_prompt, parameters):

    words = user_prompt.split()

    arguments = {}
    for key, param_type in parameters.items():
        if param_type == "number":
            for i, word in enumerate(words):

                if word.isdigit():
                    arguments[key] = int(word)
                    words.pop(i)
                    break

        elif param_type == "string":
            pass


    return arguments



prompt = "What is the sum of 2 and 3?"

parameters = {
    "a": "number",
    "b": "number"
}

print(extract_arguments(prompt, parameters))