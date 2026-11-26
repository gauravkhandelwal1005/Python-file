import turtle, colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(3)
for i in range(420):
    h = (0.12 - i / 1170) % 1
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i * 1.2)
    t.left(59)
turtle.done()
    
