# todo.md

## Day 1 - Understanding the Project

### Read the Subject

* [X] Read Chapter III (Introduction)
* [X] Read V.1 Summary
* [X] Read V.2 Input Files
* [X] Read V.3 LLM Interaction
* [X] Understand the final project goal
* [X] Understand the difference between answering a question and generating a function call

### Understand Function Calling

* [X] Explain function calling in your own words
* [X] Understand how a prompt becomes a function call
* [X] Understand why the output is JSON and not the final answer

### Understand Tokens

* [X] Learn what a token is
* [X] Understand that token != word
* [X] Learn what a token ID is
* [X] Understand why LLMs work with token IDs instead of text

### Understand LLM Generation

* [X] Learn what logits are
* [X] Understand next-token prediction
* [X] Understand how generation happens token by token
* [ ] Understand how probabilities influence token selection

### Understand Vocabulary

* [X] Learn what the vocabulary file contains
* [X] Understand token ↔ token_id mapping
* [X] Understand why the vocabulary is needed for constrained decoding

### Learn Pydantic

* [ ] Install pydantic
* [ ] Create a simple BaseModel example
* [ ] Understand validation errors
* [ ] Understand why pydantic is required in this project

### Understand Input Files

* [ ] Analyze functions_definition.json structure
* [ ] Identify function names
* [ ] Identify parameters
* [ ] Identify parameter types
* [ ] Analyze function_calling_tests.json structure
* [ ] Understand what information must be extracted from prompts

### Understand Constrained Decoding

* [ ] Read section V.3.3 carefully
* [ ] Understand why prompting alone is unreliable
* [ ] Understand valid vs invalid tokens
* [ ] Understand token filtering
* [ ] Understand how invalid logits are removed
* [ ] Understand how valid JSON is guaranteed

### Understand the SDK

* [ ] Read SDK documentation
* [ ] Understand encode()
* [ ] Understand decode()
* [ ] Understand get_logits_from_input_ids()
* [ ] Understand get_path_to_vocab_file()

### Draw Project Architecture

* [ ] Draw full project workflow on paper
* [ ] Explain the workflow without looking at the subject

### End of Day 1 Self-Test

* [ ] Can explain Function Calling
* [ ] Can explain Token
* [ ] Can explain Token ID
* [ ] Can explain Vocabulary
* [ ] Can explain Logits
* [ ] Can explain encode()
* [ ] Can explain decode()
* [ ] Can explain get_logits_from_input_ids()
* [ ] Can explain Pydantic
* [ ] Can explain Constrained Decoding
* [ ] Can explain the complete project pipeline



---



# Day 1

## Understand Project

* [ ] Read entire subject
* [ ] Understand final goal
* [ ] Understand input/output files
* [ ] Understand SDK methods
* [ ] Understand constrained decoding theory

## Environment

* [ ] Create venv with uv
* [ ] Install numpy
* [ ] Install pydantic
* [ ] Copy llm_sdk

## Exploration

* [ ] Open functions_definition.json
* [ ] Open function_calling_tests.json
* [ ] Explore vocabulary file

---

# Day 2

## Data Models

* [ ] Create Pydantic models
* [ ] FunctionDefinition model
* [ ] ParameterDefinition model
* [ ] FunctionCall model

## File Loading

* [ ] Load function definitions
* [ ] Load prompts
* [ ] Add JSON validation
* [ ] Add file error handling

---

# Day 3

## SDK Experiments

* [ ] Test encode()
* [ ] Test decode()
* [ ] Test get_logits_from_input_ids()
* [ ] Inspect vocabulary

## Understand Token Generation

* [ ] Generate next token manually
* [ ] Inspect logits
* [ ] Understand token filtering

---

# Day 4

## Constrained Decoding

* [ ] Build JSON state machine
* [ ] Restrict invalid tokens
* [ ] Generate valid JSON structure
* [ ] Validate generated fields

## Testing

* [ ] Test simple functions
* [ ] Test numbers
* [ ] Test strings

---

# Day 5

## Function Calling Logic

* [ ] Build prompt template
* [ ] Let LLM choose function
* [ ] Extract arguments
* [ ] Validate arguments

## Output

* [ ] Create output objects
* [ ] Export JSON file

---

# Day 6

## Finalization

* [ ] Test full pipeline
* [ ] Edge case testing
* [ ] Large numbers
* [ ] Empty strings
* [ ] Invalid prompts
* [ ] Missing files

## Documentation

* [ ] README
* [ ] Algorithm explanation
* [ ] Design decisions
* [ ] Performance analysis
* [ ] Testing strategy

## Final Check

* [ ] flake8
* [ ] mypy
* [ ] make run
* [ ] make lint
* [ ] make clean
