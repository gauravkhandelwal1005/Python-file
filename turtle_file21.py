from turtle import *
from colorsys import *
tracer(5)
bgcolor("black")
pensize(2)
h = 1
for i in range(140):
    h -= 0.0071
    color(hsv_to_rgb(h, 1, 1))
    goto(20, 10)
    right(70)
    forward(i*2)
    circle(i*2, -10)
    left(100)
    up()
    forward(i)
    down()
    circle(90, -90)
    right(230)
done()
