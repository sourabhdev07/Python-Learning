import json 
from types import SimpleNamespace

with open("student.json" , "r" , encoding="utf-8") as file:
    
    data = json.load(file , object_hook= lambda d:SimpleNamespace(**d))
    
    print(data.name)
    print(data.salary)
    
# SimpleNamespace is built -in light-weighted python object    