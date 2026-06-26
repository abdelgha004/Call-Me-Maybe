

def build_prompt(functions, user_prompt):

    result = "You are a function calling assistant.\n\n"
    result += "Available functions:\n"

    for func in functions:
        result += f"\nFunction: {func['name']}\n"
        result += f"Description: {func['description']}\n"
        result += f"Parameters:\n"
        for param_name, param_info in func["parameters"].items():
            result += f"- {param_name}: {param_info['type']}\n"

    result += f"\nUser request:\n{user_prompt}\n\n"

    result += "Instructions:\n"
    result += "- Choose exactly one function.\n"
    result += "- Respond only with the function name."
    return result