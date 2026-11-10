import json

FILE_NAME = "student.json"

student = {
    "name" : "Sourabh",
    "age" : 26,
    "city" : "Indore"
}

with open(FILE_NAME , "w", encoding="utf-8") as file:
    
    # json.dump(student, file)
    json.dump(student, file , indent=4)
    
    
# input python object -> output : json File 