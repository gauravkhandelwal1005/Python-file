from turtle import *
import colorsys

tracer(10)
bgcolor("black")
pensize(1)
speed(0)

def star_fractal(length, depth):
    if depth == 0:
        return 
    
    h = 0.55 * depth * 0.035
    color(colorsys.hsv_to_rgb(h % 1, 1, 1))
    
    for _ in range(6):
        forward(length)
        star_fractal(length * 0.4, depth - 1)
        backward(length)
        right(60)
        
penup()
goto(0, 100)
pendown()

star_fractal(100, 5)
done()
