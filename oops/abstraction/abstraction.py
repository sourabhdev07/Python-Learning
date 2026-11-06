from abc import ABC , abstractmethod

class Shape(ABC):    
    
    def __init__(self , r):
        self.r = r
        
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def area(self):
        return 3.14 * (self.r**2)
    
    
c = Circle(2)
# s = Shape(2)
print(c.area())    


