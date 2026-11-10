# import csv

# with open("excel.csv", "a" , newline="" , encoding="utf-8") as file:
    
#     writer = csv.writer(file)
    
#     writer.writerow(["Yash" , 24 , "Indore"])

import csv

with open("excel.csv", "r", newline="", encoding="utf-8") as file:

    reader = csv.reader(file , delimiter=";")

    for row in reader:
        print(row)