# Create a parent class Vehicle with a method:

# start() → prints "Vehicle is starting"

# Create a child class Car that overrides start() and prints:

# "Car engine is starting"

class Vehicle:
    
    def start(self):
        print( "Vehicle is starting")
    
class Car(Vehicle):
    
    def start(self):
        super().start()
        return "Car engine is starting"

c1 = Car()

print(c1.start())