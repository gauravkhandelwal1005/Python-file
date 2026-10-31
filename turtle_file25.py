from turtle import *
from colorsys import *
tracer(5)
bgcolor("black")
pensize(2)
h = 0.5
for i in range(155):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.004
    for j in range(4):
        fd(i)
        right(20)
        right(60)
    right(120)
done()
