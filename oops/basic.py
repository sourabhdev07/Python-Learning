# Q1. Create a Car class with these attributes:
# - brand = "Maruti"
# - color = "Red"
# - model = "Swift"
# Create an object and print all three attributes.

class Car:
    
    brand = "Maruti"
    color = "Red"
    model = "Swift"
    
c1 = Car()

# print(c1.brand)    
# print(c1.color)    
# print(c1.model)    

# Q2. Create a Calculator class with two methods:
# - add() – Add two numbers.
# - multiply() – Multiply two numbers.

class Calculator:
    def add(self , x , y):
        self.x = x
        self.y = y
        return x + y
    
    def multiply(self , a , b):
        self.a = a
        self.b = b
        return (self.a) * (self.b)
        
c1 = Calculator()

# print(c1.add(2, 4))        
# print(c1.multiply(2, 5))   


# Can we create 10 objects from one class? Explain with code.

class Student:
    def print_student(self, name , age):
        # name = name
        # self.age = age
        # self.name = name
        # self.age = age
        return f"My name is {name} and age is {age}"
    
    
s1 = Student()           
s2 = Student()           

# print(s1.print_student("Sourabh" , 26))        
# print(s2.print_student("Rahul" , 25))       

class Student:

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

s1 = Student("Rahul")
s2 = Student("Amit", 23)

print(s1.name, s1.age)
print(s2.name, s2.age) 