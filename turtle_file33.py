import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.speed(0)

colors = ["red", "green", "pink", "blue"]

for i in range(180):
    t.pencolor(colors[i % 4])
    t.forward(i * 1.5)
    t.left(92)
    
turtle.done()
