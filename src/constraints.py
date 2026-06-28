from llm_sdk import Small_LLM_Model


class Constraints:
    def __init__(self):
        self.model = Small_LLM_Model()

    def build_function_tokens(self, functions):
        function_tokens = {}
        for func in functions:
            name = func["name"]
            token = self.model.encode(name)
            token_ids = token[0].tolist()
            function_tokens[name] = token_ids
        return function_tokens
    
    def get_allowed_tokens(self, function_tokens, generated_ids):
        allowed = []

        for token_ids in function_tokens.values():

            if token_ids[:len(generated_ids)] == generated_ids:

                if len(generated_ids) < len(token_ids):

                    next_token = token_ids[len(generated_ids)]
                    if next_token not in allowed:
                        allowed.append(next_token)
        return allowed
