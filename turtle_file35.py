from turtle import * 
speed(0)
bgcolor("black")
c = ["red", "yellow", "green",
     "purple", "orange", "blue"]
hideturtle()
for i in range(140):
    pencolor(c[i % 6])
    width(i / 30)
    forward(i)
    left(120)
    for j in range(2):
        forward(i)
        right(90)
done()
