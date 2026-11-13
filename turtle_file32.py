from turtle import *
import colorsys as cs
bgcolor("black")
speed(0)
tracer(100)

h = 0
goto(150, 50)
for i in range(200):
    color(cs.hsv_to_rgb(h, 1, 1))
    for j in range(75):
        h += 0.005
        fd(100)
        bk(100)
        rt(2)
        
    fd(250)
done()
          
