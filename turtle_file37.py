from turtle import *
tracer(2)
bgcolor("black")
colors = ["white", "red"]
for i in range(220):
    color(colors[i % 2])
    rt(i)
    circle(200, i + 2)
    fd(i)
    right(180)
    fd(i)
hideturtle()
done()
