# Convert "250" into an integer and add 50.
a = "250"
b = int(a) + 50
print(b)

# Create a list of five numbers. Print the first and last elements.
a = [1, 4, 5, 3 , 6]
print(a[0])
print(a[-1])

# Create a tuple of five fruits. Try to modify its first element. What happens?
a = ("orange" , "papaya" , "banana" , "strawberry")
# a.update("orange" , "yellow")
print(a)

# Create a set containing duplicate numbers. Print the result.
a = set({1 , 2, 3,3, 5, 4 , 1 })
print(a)


# Add 60, remove 20 and print the final list.
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
numbers.remove(20)
print(numbers)


# Find their union, intersection and difference.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
## --- outputs --- ##
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}
# {1, 2, 5, 6}


# Create a dictionary for an employee with name, age, salary and city. Print each value.

employee = {
    "name" : "Sourabh",
    "age" : 25,
    "city" : "Indore"
}

print(employee["name"])
print(employee["age"])
print(employee["city"])

# Print:
# - First six characters.
# - Last six characters.
# - Reverse string.
# - String in uppercase.
name = "Python Programming"
# print(name[0:7])
# print(name[-1:-7])
print(name[::-1])
print(name.upper())