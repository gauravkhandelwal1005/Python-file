class Calculator:
  def __init__(self, n):
    self.n = n

  def square(self):
    print(f"The square is {self.n*self.n}")

  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")

  def squareroot(self):
    print(f"The square root is {self.n**1/2}")



a = Calculator(4)
a.square()
a.cube()
a.squareroot()

class Meta(type):
  def __new__(mcls, name, bases, namespace):
    namespace["value"] = 100
    return super().__new__(mcls, name, bases, namespace)

class A(metaclass=Meta):
  value = 10

class B(A):
  pass

print(A.value, B.value)

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Square(shape):
    def __init__(self, side):
        self.side = side
 
    def area(self):
        return self.side * self.side

s = Square(4)
print(f"Area of square is {(s.area())}")

