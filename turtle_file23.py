from turtle import *

tracer(20)
bgcolor("black")

colors = [
    (255, 0, 0),
    (255, 100, 0),
    (255, 165, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 100, 255),
    (0, 0, 255),
    (138, 43, 226),
    (255, 0, 255),
    (255, 20, 147),
]

colormode(255)

for i in range(400):
    pencolor(colors[i % len(colors)])
    right(119)
    circle(-i * 0.3, 120)
    circle(i * 0.3, 120)
    circle(-i * 0.1, 120)

done()
