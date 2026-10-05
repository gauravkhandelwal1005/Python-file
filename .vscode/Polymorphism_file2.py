class Order:
    def __init__(self, item, price):
    self.item = item
    self.price = price

def __gt__(self, num2):
    return self.price > num2.price

ord1 = Order("Chips", 20)
ord2 = Order("Tea", 15)
print(ord1 > ord2)
    
       
