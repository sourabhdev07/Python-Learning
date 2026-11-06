# import csv

# with open("excel.csv" , "r" , newline="" , encoding="utf-8") as file:
    
#     reader = csv.reader(file)
    
#     for row in reader:
#         print(row)

import csv

# with open("excel.csv", "r", newline="", encoding="utf-8") as file:

#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
        
#         import csv

with open("excel.csv", "r", newline="", encoding="utf-8-sig") as file:

    reader = csv.reader(file)

    header = next(reader)

    print("Headers:", header)

    for row in reader:
        print(row)