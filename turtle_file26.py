from turtle import *
tracer(10)
bgcolor("black")
colors = ["white", "orange"]
for i in range(205):
    color(colors[i % 2])
    rt(i)
    circle(200, i + 2)
    fd(i)
    right(180)
    fd(i)
    hideturtle()
done()
