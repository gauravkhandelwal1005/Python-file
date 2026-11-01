import turtle
import math
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

for i in range(500):
    a = i * 0.12
    r = 100 + 80 * math.sin(5 * a)
    
    x = r * math.cos(a)
    y = r * math.sin(a) * 0.7
    
    t.pencolor(colorsys.hsv_to_rgb(i/500, 1, 1))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(4)
    
turtle.done()
