import turtle
from math import sin, cos as c
t = turtle.Turtle(); t.speed(0)
turtle.bgcolor("black"); t.width(4)
def heart(a, s):
    y = 13*c(a)-5*c(2*a)-2*c(3*a)
    return 16*s*sin(a)**3, s*y
def loop(a, s):
    return 16*s*c(a), 9*s*sin(2*a)
def go(f, s, col):
    t.penup(); t.color(col)
    for i in range(0, 363, 3):
        t.goto(*f(i / 57.3, s))
        t.pendown()
for k in range(14):
    go(loop, 22-k/2, (k/14, .3, 1))
for k in range(31):
    go(heart, 8-k/4, (1, 0, k/40))
