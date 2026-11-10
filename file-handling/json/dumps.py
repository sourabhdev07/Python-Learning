import json 

student = {
    "name" : "hello",
    "age" : 33
}

json_data = json.dumps(student ,  indent=4)

print(json_data)
print(type(json_data))    # str

# Definition: json.dumps() converts a Python object into a JSON-formatted string.
# Useful : when you need to send JSON data to another application or API. 