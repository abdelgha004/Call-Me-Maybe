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

        if param_type["type"] == "number":
            for i, word in enumerate(words):
                
                clean_word = word.strip("?,.!")

                if clean_word.isdigit():
                    arguments[key] = int(clean_word)
                    words.pop(i)
                    break
        elif param_type["type"] == "string":
            value = extract_string(user_prompt)
            if value:
                arguments[key] = value

        elif param_type == "boolean":
            for i, word in enumerate(words):
                clean_word = word.strip("?,.!").lower()
                if clean_word == "true":
                    arguments[key] = True
                    words.pop(i)
                    break

                elif clean_word == "false":
                    arguments[key] = False
                    words.pop(i)
                    break
    return arguments

