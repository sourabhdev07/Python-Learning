# Create employees.csv with name, age and salary columns.
# Read and print all employee records using csv.reader().

import os
import csv

FILE_NAME = "employees.csv"

with open(FILE_NAME , "a" , newline="" , encoding="utf-8") as file:
    
    try:
        
        reader = csv.writer(file)
        
        for row in reader(file):
            print(row)
            
    except FileNotFoundError:
        
        print("not Found")        