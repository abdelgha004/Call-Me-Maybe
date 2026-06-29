

def validator(arguments, parameters):
    for param in parameters:
        if param not in arguments:
            return False

    for arg in arguments:
        if arg not in parameters:
            return False
    
    for param in parameters:
        param_type = parameters[param]["type"]
        arg_valuo = arguments[param]

        if param_type == "number":
            if type(arg_valuo) != int and type(arg_valuo) != float:
                return False
        elif param_type == "string":
            if type(arg_valuo) != str:
                return False
        else:
            return False
    return True
