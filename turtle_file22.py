import turtle 
import colorsys
screen = turtle.Screen()
screen.bgcolor("#050505")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)
for i in range(180):
    hue = i / 180.0
    color = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    t.pencolor(color)
    t.circle(1 * 1.5, 90)
    t.left(90)
    t.circle(i * 1.5, 90)
    t.left(20)
turtle.done()
