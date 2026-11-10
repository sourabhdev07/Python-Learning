import csv

with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Sourabh", 25])

with open("test.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    
    # reader.

    for row in reader:
        # print(row["Name"])
        print(row)