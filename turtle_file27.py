from turtle import *
from colorsys import *

setup(750, 800)
tracer(50)
bgcolor("black")

h = 0

for i in range(225):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.01
    
    for j in range(4):
        circle(30 + j * 4, -90)
        fd(300)
        rt(90)
        circle(10)
        
    rt(10)
done()
