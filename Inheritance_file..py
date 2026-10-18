class Car:
  @staticmethod
  def start():
      print("Car is started")

  @staticmethod
  def stop():
      print("Car is stop")

class Toyato(Car):
  def __init__(self, name, brand):
    self.name = name 
    self.brand = brand

class Fortuner(Toyato):
  def __init__(self, name, brand, type):
    super().__init__(name, brand)
    self.type = type

c1 = Fortuner("Fortuner Legender", "Toyato", "SUV")
print(c1.name, c1.brand, c1.type)
c1.start()
