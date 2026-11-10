import json

json_data = '{"name": "Sourabh", "age": 25, "marks": 85}'

student = json.loads(json_data)

# print(json_data["name"]) --> TypeError
print(student["name"])
print(student.get("age"))
print(type(student))

# Definition: json.loads() converts a JSON-formatted string into a Python object.
# Useful : access the data from API