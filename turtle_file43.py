import turtle
from colorsys import hsv_to_rgb
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
for r in range(10, 370, 5):
    c = hsv_to_rgb(r / 440, 1, 1)
    t.pencolor(c)
    t.penup()
    t.goto(0, 0)
    t.setheading(r / 4)
    t.forward(r)
    t.right(162)
    t.pendown()
    for _ in range(5):
        t.forward(r * 1.902)
        t.right(144)
        
