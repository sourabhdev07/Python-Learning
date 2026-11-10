import json

FILE_NAME = "student.json"

with open(FILE_NAME , "r", encoding="utf-8") as file:
    
    data = json.load(file)
    
    print(data)
    print(data["name"])
    print(type(data))
    
# input: Json File --> output: python Object ( Dict )     