import turtle
from math import sin, cos, pi
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0); t.pensize(4)
def heart(k, dx, c):
    t.pencolor(c); t.penup()
    for i in range(121):
        a = i * pi / 60
        x = 16 * sin(a) ** 3
        y = 13*cos(a) - 5*cos(2*a) 
        y -= 2*cos(3*a) + cos(4*a)
        t.goto(dx + k*x, k*y)
        t.pendown()
for k in range(4, 16, 2):
    heart(k, -90, (1, .8-k/25, .8))
    heart(k, 90, (1, .4-k/40, .2))
    
turtle.done()
