import turtle, random
from colorsys import hsv_to_rgb
random.seed(7)
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.speed(0); t.pensize(7)
t.color("#7CFC00"); t.goto(0, -330)
t.pensize(2)
for i in range(60):
    a = i*6 + random.random()*4
    t.penup(); t.home(); t.seth(a)
    t.pendown(); t.color("white")
    t.fd(random.randint(150, 185))
    t.color(hsv_to_rgb(i/60, .4, 1))
    for f in range(-45, 46, 115):
        t.seth(a + f)
        t.fd(28); t.bk(28)
t.up(); t.home(); t.dot(40, "gold")
turtle.done()
