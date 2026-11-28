import turtle
turtle.setup(800, 900)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

colors = ["yellow", "red", "yellow", "red"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(150 - i, 100)
        turtle.lt(90)
        turtle.circle(150 - i, 100)
        turtle.rt(60)
        
turtle.mainloop()
