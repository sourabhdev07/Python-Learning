import csv

with open("excel.csv", "r", newline="", encoding="utf-8-sig") as file:
    
# newline="" , it remove the extra spaces from csv 
# The csv module writes a standard Windows line ending: \r\n.

# Python's open() (without newline="") automatically replaces every \n it sees with \r\n.

# The result: \r + \r\n becomes \r\r\n.

# How text editors read \r\r\n:

# The first \r pushes the cursor back to the start of the line.

# The \r\n moves it down to a new empty line, which is why you end up with unwanted blank rows between your CSV records.

    reader = csv.reader(file)
    
    header = next(reader)
#  - next(reader) gets the first row.
# - The loop starts from the second row.

    print("Headers:", header)

    for row in reader:
        print(row)