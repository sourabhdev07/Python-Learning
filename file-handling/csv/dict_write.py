import csv

students = [
    {"name" : "Sourabh" , "age" : 23 , "city":"Indore"},
    {"name" : "Rahul" , "age" : 26 , "city":"Indore"},
    {"name" : "Amit" , "age" : 26 , "city":"Bhopal"}
]

with open("excel.csv" , "w" , newline="" , encoding="utf-8") as file:
    
    fieldnames = ["name" , "city" , "age" ]
    
    writer = csv.DictWriter(file , fieldnames=fieldnames)
    
    writer.writeheader()
    
    writer.writerows(students)
    
    
# Important methods
# - fieldnames: Defines CSV column names and their order.
# - writeheader(): Writes the header row.
# - writerow(): Writes one dictionary.
# - writerows(): Writes multiple dictionaries.