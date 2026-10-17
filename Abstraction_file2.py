class Calculator:
  def __init__(self, n):
    self.n = n

  def square(self):
    print(f"The square is {self.n*self.n}")

a = Calculator(4)
a.square()
