import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
colors = ["cyan", "magenta", "lime", "yellow", "orange"]

for i in range(250):
    t.color(colors[i % 5])
    t.forward(i)
    t.left(59)
    
turtle.done()
    
