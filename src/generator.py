from llm_sdk import Small_LLM_Model



class Generator:
    def __init__(self):
        self.model = Small_LLM_Model()

    def get_logits(self, prompt):

        tokens = self.model.encode(prompt)

        input_ids = tokens[0].tolist()

        logits = self.model.get_logits_from_input_ids(input_ids)

        return logits
    
    def generate(self, prompt, functions, max_tokens=100):
        result = prompt
        function_names = [
            func["name"] for func in functions
        ]

        for _ in range(max_tokens): 
            logits = self.get_logits(result)

            top_score = max(logits)
            top_token = logits.index(top_score)

            token = self.model.decode([top_token])
            print("TOKEN:", repr(token))

            result += token
            print("RESULT:", result)
            generated = result.strip()

            for name in function_names:
                if generated.endswith(name):
                    return name
        return None