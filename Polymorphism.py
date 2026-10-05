class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real, "i", self.img, "j")
        
    def __add__(self, num2):
        real =self.real + num2.img
        img = self.real + num2.img
        return Complex(real, img)
    
num1 = Complex(2, 3)
num2 = Complex(4, 5)

num3 = num1.add(num2) #num3 = num1 + num 2
num3.showBumber()
