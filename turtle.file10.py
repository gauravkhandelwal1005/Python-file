from turtle import * 
from colorsys import *
setposition(0, -45)
bgcolor("black")
tracer(2)
h = 0
def square(x):
    for i in range(4):
        fd(x)
        lt(90)

def shape(x):
    fd(x)
    lt(45)
    fd(x)
    rt(60)
    width(3)
    square(x)
    width(1)
    rt(165)
    fd(x)
    lt(45)
    fd(x)
    
for i in range(300):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.0045
    circle(50, 4)
    rt(90)
    shape(70)
    rt(135)
    hideturtle()
done()
