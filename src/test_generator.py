from src.generator import Generator


functions = [
    {
        "name": "fn_add_numbers"
    },
    {
        "name": "fn_greet"
    }
]


generator = Generator()


result = generator.generate(
    "What is 2 + 3?",
    functions
)


print(result)