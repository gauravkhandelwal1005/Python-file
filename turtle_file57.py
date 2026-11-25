import turtle
from math import *
t = turtle.Turtle(); t.speed(0)
turtle.Screen().bgcolor("black")
P = []
for i in range(181):
    a = i * pi / 90
    r = exp(cos(a)) - 2*cos(4*a)
    P.append((r*sin(a), r*cos(a)))
S = [*range(5, 80, 2), 30, 52, 80]
for s in S:
    t.color(s%2, s%2*s/110, 0)
    t.width(7 if s % 2 else s / 7)
    for x, y in P:
        t.goto(s*x, s*y)
for x, y in P[::3]:
    t.up(); t.goto(80*x, 80*y)
    t.dot(x*x + y*y, "white")
