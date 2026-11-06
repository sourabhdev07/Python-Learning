# file = open("name.txt" , "r")

# data = file.read()

# print(data)

# file.close()

# import os

# print(os.getcwd())

# if os.path.exists("name.txt"):
#     print("File exists")
# else:
#     print("File does not exist")

import os

# os.mkdir("students")
# os.rename("name.txt" , "student.txt")

isP = os.path.isfile("student.txt")
isP1 = os.path.isdir("students")
print(isP)
print(isP1)