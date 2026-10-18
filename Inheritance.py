class Car:
  @staticmethod
  def start():
    print("Car is started")

  @staticmethod
  def stop():
    print("Car is stopped")

class Toyato(Car):
    def __init__(self, name):
    self.name = name 

c1 = Toyato("Fortuner")
c2 = Toyato("Innova")

print(c1.name)
print(c2.name)  
Car.start())
    
    
    
      
