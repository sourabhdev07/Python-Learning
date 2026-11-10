import csv

# with open("excel.csv" , "w" , newline="" , encoding="utf-8-sig") as file:
    
#     writer = csv.writer(file)
    
#     writer.writerow(["name" , "age" , "city"])
    
#     writer.writerow(["Sourabh", 25, "Indore"])
#     writer.writerow(["Rahul", 24, "Bhopal"])
#     writer.writerow(["Amit", 23, "Dewas"])

# multiple row writerows()

students = [
    ["Sourabh Namdev" , 34],
    ["Abhi Namdev" , 23 , "Indore"]
]


with open("excel.csv" , "w" , newline="" , encoding="utf-8-sig") as file:
    
    writer = csv.writer(file)
    
    writer.writerow(["name" , "age" , "city"])
    
    writer.writerows(students)
    

