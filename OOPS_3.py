class Object:
  def __init__(self):
    self.value = 10

  def _getattribute_(self, name):
    if name == "value":
      return 99
    return object._getattribute_(self, name)

a = Object()
print(a.value, a.dict__("value"))
