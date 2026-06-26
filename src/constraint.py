from llm_sdk import Small_LLM_Model


class ConstraintBuilder:
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