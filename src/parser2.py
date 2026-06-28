def extract_string(prompt):

    if "'" in prompt:
        start = prompt.find("'")
        end = prompt.find("'", start + 1)

        return prompt[start + 1:end]

    elif '"' in prompt:
        start = prompt.find('"')
        end = prompt.find('"', start + 1)

        return prompt[start + 1:end]

    return None

def extract_arguments(user_prompt, parameters):

    words = user_prompt.split()

    arguments = {}
    for key, param_type in parameters.items():

        if param_type == "number":
            for i, word in enumerate(words):
                
                clean_word = word.strip("?,.!")

                if clean_word.isdigit():
                    arguments[key] = int(clean_word)
                    words.pop(i)
                    break
        elif param_type == "string":
            value = extract_string(user_prompt)
            if value:
                arguments[key] = value

    return arguments



prompt = "What is the sum of 2 and 3?"

parameters = {
    "a": "number",
    "b": "number"
}

print(extract_arguments(prompt, parameters))

print(extract_arguments(
    "Reverse the string 'hello'",
    {"s": "string"}
))