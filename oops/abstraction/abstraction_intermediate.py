# Question 2 – Intermediate
# Intermediate
# Create an abstract class Employee.

# Requirements:
# - Constructor: name, salary.
# - Abstract method: calculate_bonus().
# - Normal method: display_details().
# Create two child classes:
# - Developer: bonus = 10% of salary.
# - Manager: bonus = 20% of salary.
# Create both objects and display their details and bonuses.

from abc import ABC , abstractmethod

class Employee(ABC):
    
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
        
    @abstractmethod
    def calculate_bonus(self):
        pass
    
    def display_details(self):
        return f"name:{self.name} and salary:{self.salary}"
    
class Developer(Employee):
    
    def calculate_bonus(self):
        return self.salary * 0.1
    
class Manager(Employee):
    
    def calculate_bonus(self):
        return self.salary * 0.2
    
    
d = Developer("Sourabh Namdev" , 10000)
m = Manager("Boss Sourabh" , 20000)

print(d.display_details())
print(d.calculate_bonus())

print(m.display_details())
print(round(m.calculate_bonus()))
     
            