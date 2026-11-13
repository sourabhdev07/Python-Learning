import csv
import os

FILE_NAME = "student.csv"

def add_student(name, age, marks):
    
    file_exists = os.path.exists(FILE_NAME)
    
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        
        fieldnames = ["name" , "age", "marks"]
        
        writer = csv.DictWriter(file , fieldnames=fieldnames)
        
        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writeheader()
            
        writer.writerow({
            "name": name,
            "age": age,
            "marks": marks
        })

    print("Student added successfully")   
    
def display_all():
    
    try:
        with open(FILE_NAME , "r" , newline="", encoding="utf-8" ) as file:
            
            reader = csv.DictReader(file)
            
            
            for row in reader:
                # if row > 25:
                    print(row)
        
    except FileNotFoundError:
         print("File doesn't found")
                  
    

# add_student("Sourabh", 26, 78)
# add_student("Rahul", 23, 88)  

display_all()