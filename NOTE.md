# note.md

# Call Me Maybe - Notes

## Project Goal

The goal is NOT to execute functions.

The goal is to convert a natural language prompt into a structured function call.

Example:

Prompt:
"What is the sum of 2 and 3?"

Output:
{
"prompt": "What is the sum of 2 and 3?",
"name": "fn_add_numbers",
"parameters": {
"a": 2,
"b": 3
}
}

---

# Important Concepts

## 1. Function Calling

Function calling means:

Natural language
↓
LLM understanding
↓
Function name + parameters
↓
JSON output

The model should choose:

* Which function to call
* Which arguments to extract

---

## 2. JSON

Must know:

* object {}
* array []
* strings
* numbers
* booleans

Examples:

{
"name": "fn_greet",
"parameters": {
"name": "John"
}
}

---

## 3. Pydantic

Required by subject.

Use it to:

* validate input data
* validate output data
* enforce parameter types

Example:

class FunctionCall(BaseModel):
prompt: str
name: str
parameters: dict

---

## 4. Constrained Decoding

Most important concept in project.

Without constrained decoding:

LLM may generate invalid JSON.

With constrained decoding:

Only valid tokens are allowed.

Process:

1. Get logits
2. Check allowed tokens
3. Block invalid tokens
4. Choose next token
5. Repeat

Goal:

100% valid JSON output.

---

## 5. Vocabulary File

SDK provides:

get_path_to_vocab_file()

Vocabulary maps:

token_id
↔
token_text

Needed to know which tokens are valid during generation.

---

## 6. SDK Methods

encode(text)

Convert text → token ids.

decode(token_ids)

Convert token ids → text.

get_logits_from_input_ids(ids)

Get model predictions.

get_path_to_vocab_file()

Get vocabulary file path.

---

## 7. Input Files

functions_definition.json

Contains:

* function names
* descriptions
* parameters
* return type

function_calling_tests.json

Contains prompts.

---

## 8. Output File

Required format:

[
{
"prompt": "...",
"name": "...",
"parameters": {}
}
]

Rules:

* valid JSON
* no extra keys
* correct types
* all parameters present

---

## 9. Error Handling

Handle:

* missing files
* invalid JSON
* invalid schema
* empty files

Program should never crash.

---

## 10. Evaluation Focus

Expect questions about:

* Why constrained decoding?
* How token generation works?
* How SDK works?
* Why pydantic?
* How function selection is done?
* How JSON validity is guaranteed?
