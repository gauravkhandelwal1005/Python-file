import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

for i in range(180):
    t.forward(i * 2)
    t.right(59)
    t.circle(30)
    
turtle.done()
