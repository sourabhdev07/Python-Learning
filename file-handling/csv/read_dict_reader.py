# Definition: csv.DictReader() reads each CSV row as a dictionary, using the header row as dictionary keys.

import csv 

with open("excel.csv" , "r" , newline="" , encoding="utf-8-sig") as file:

    reader = csv.DictReader(file , delimiter=";")

    for row in reader:
        print(row)
        
# By the help of this we can access values directly from column name not indexing.