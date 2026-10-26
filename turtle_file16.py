from turtle import * 
from colorsys import * 
import math

tracer(0)
bgcolor("black")
pensize(1.5)

h = 0.6

for i in range(400):
    h += 0.0025
    c = hsv_to_rgb(h % 1, 0.9, 1)
    color(c)
    
    goto(0, 0)
    circle(180 - i/2, 120)
    
    goto(0, 0)
    circle(60 + i/3, 60)
    
    goto(0, 0)
    rt(2)
    fd(i * 0.15)
    dot(3 * math.sin(1/10)*2)
    
    if i % 2 == 0:
        update()
done()
    
