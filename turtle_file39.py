from turtle import *
from colorsys import *
from math import sin

setup(700, 700); bgcolor("black")
tracer(1, 10); ht(); speed(0)

for i in range(180):
    color(hsv_to_rgb(0.7 * abs(sin((i + 15) / 30)), 1, 1))
    pensize(2 if i < 60 else 1)
    circle(3 - i, 80); rt(160); circle(i, 80); lt(80)
    
done()
