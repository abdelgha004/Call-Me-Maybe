## Day 1 — Constrained Decoding Core (parameters)

- [ ] Fhem structure dyal vocab.json (get_path_to_vocab_file) - jarreb encode/decode
      o chouf kifach kaybane token m3a "Ġ" (space prefix)
- [ ] Bni id_to_token dict wahda (mn vocab file, machi decode() wahda b wahda)
- [ ] Bdel function name selection bach ykhdem b vocab dict bdal encode() m3zoul
- [ ] Kteb generate_number() - mask 3la digits/./- , wa9ef mnin unconstrained
      top token machi numeric
- [ ] Kteb generate_string() - mask 3la kolchi machi quote/control char,
      wa9ef mnin unconstrained top = quote closer
- [ ] Kteb generate_boolean() - trie 3la "true"/"false" (nafs manti9 dyal function names)
- [ ] Test wahed b wahed b script sahel (bla pipeline kamla) - t2akked kol wahda
      khedama m3azola 9bel matdkhelha f generator

## Day 2 — Wire everything + robustness

- [ ] Dmej koulchi f Generator.generate() : function selection -> loop 3la
      parameters (b type dyal kol wahed) -> build result dict
- [ ] Sewweb __main__.py: 7yed import dyal validator/parser, sewweb pipeline
      bach ykhdem b generation jdida
- [ ] Sewweb cli.py default paths (data/output/function_calling_results.json)
- [ ] Jarreb b l 5 exemples dyal function_calling_tests.json - chouf output
- [ ] Zid edge cases: negative numbers, floats, multi-param same type,
      empty string, special characters
- [ ] Sewweb bugs li ghatban (tokenizer edge cases, infinite loop guard,
      timeout/max_tokens)
- [ ] Handle missing/malformed functions_definition.json o input file
      (try/except mzyan, message wadeh, machi crash)

## Day 3 — Compliance + polish

- [ ] Zid pydantic models (FunctionDefinition, Parameter, TestPrompt, Result...)
- [ ] Zid type hints f kolchi (functions, returns, variables)
- [ ] Zid docstrings (Google/NumPy style) f kol function/class
- [ ] Kteb Makefile: install / run / debug / clean / lint / lint-strict
- [ ] Run flake8 . o mypy . --strict - sewweb kolchi li khareج
- [ ] Zid .gitignore (pycache, .mypy_cache, data/output/...)
- [ ] git rm --cached data/output/function_calling_results.json
- [ ] Kteb README.md: first line b login, Description, Instructions,
      Resources+AI usage, Algorithm explanation, Design decisions,
      Performance analysis, Challenges faced, Testing strategy, Example usage
- [ ] Final test: uv sync mn zero (b7al reviewer) + run kamel + verifie JSON output