class Car:

    def __init__(self):
        pass
    
    def start(self):
        print("Start car")
        
    def stop(self):
        print("Stop Car")    


class Maruti(Car):
    
    def __init__(self , speed):
        self.speed = speed
       
    def getCarSpeed(self):
        return self.speed  
            
c1 = Maruti(70)        

print(c1.start())    
print(c1.getCarSpeed())    
print(c1.stop())    
        