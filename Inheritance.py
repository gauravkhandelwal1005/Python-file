class Car:
  @staticmethod
  def start():
    print("Car is started)

  @staticmethod
  def stop():
    print("Car is stopped")

class Toyato(Car):
    def __init__(self, name):
    self.name = name 

c1 = ToyatoCar("Fortuner")
c2 = ToyatoCar("Innova")

print(c1.name)
print(c2.name)  
print(car.start())
    
    
    
      
