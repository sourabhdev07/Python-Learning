# Create two classes:
# - Car with method start() → "Car is starting"
# - Bike with method start() → "Bike is starting"
# Create one object of each class and call the same method.

class Car:
    
    def start(self):
        print("Car is starting")
        
        
class Bike():
    
    def start(self):
        print("Bike is Starting")
        
car = Car()
bike = Bike()

car.start()
bike.start()        
    
        