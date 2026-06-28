from llm_sdk import Small_LLM_Model
from .constraints import Constraints


class Generator:
    def __init__(self):
        self.model = Small_LLM_Model()
        self.constraint = Constraints()

    def get_logits(self, prompt):

        tokens = self.model.encode(prompt)

        input_ids = tokens[0].tolist()

        logits = self.model.get_logits_from_input_ids(input_ids)

        return logits
    
    def select_token(self, logits, allowed_token):
        
        allowed_score = {}
        for token_id in allowed_token:
            allowed_score[token_id] = logits[token_id]

        best_token = max(allowed_score, key=allowed_score.get)

        return best_token



    def generate(self, prompt, functions, max_tokens=100):
        result = prompt
        # function_name = [func["name"] for func in functions]

        function_token = self.constraint.build_function_tokens(functions)
        generated_ids = []
        for _ in range(max_tokens): 
            logits = self.get_logits(result)
            allowed_token = self.constraint.get_allowed_tokens(
                function_token, generated_ids
            )
            if not allowed_token:
                break

            next_token_id = self.select_token(logits, allowed_token)

            generated_ids.append(next_token_id)

            result += self.model.decode([next_token_id])

        return self.model.decode(generated_ids)
            # token = self.model.decode([top_token])
            # print("TOKEN:", repr(token))

            # result += token
            # print("RESULT:", result)
            # generated = result.strip()

            # for name in function_name:
            #     if generated.endswith(name):
            #         return name
        # return None