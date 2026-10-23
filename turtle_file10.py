import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)
t.width(2)

h = 0

for i in range(220):
    t.pencolor(colorsys.hsv_to_rgb(h, 1, 1))
    
    for _ in range(5):
        t.forward(i * 2)
        t.right(144)
        
    t.right(3)
    h += 0.006
    
turtle.done()
