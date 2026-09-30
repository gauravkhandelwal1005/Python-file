import turtle

t = turtle.Turtle()
t.forward(50)
t.left(45)
t.forward(30)
print("Position:", t.position())
print("Heading:", t.heading())
print("Is pen down", t.isdown())
print("Distance from orgin:", t.distance(0,0))
turtle.done()
