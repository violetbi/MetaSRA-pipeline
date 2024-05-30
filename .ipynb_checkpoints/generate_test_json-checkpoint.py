import json

data = [
    {
        "ID": "P352_141",
        "age": "48",
        "bmi": "24",
        "gender": "female",
        "source_name": "vastus lateralis muscle_female",
        "tissue": "vastus lateralis muscle"
    },
    {
        "ID": "P352_141",
        "age": "29",
        "bmi": "30",
        "gender": "male",
        "source_name": "vastus lateralis muscle_female",
        "tissue": "vastus lateralis muscle"
    }
]

# Write the data to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
