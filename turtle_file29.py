import turtle
screen = turtle.Screen()
screen.setup(1280, 1024)
screen.bgcolor("#10002B")
screen.title("Neon Spiral Art")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

COLOR_1 = "#00F5FF"
COLOR_2 = "#FF00FF"

for i in range(20):
    t.color(COLOR_1)
    t.circle(90, 90)
    t.left(-530)
    
    t.color(COLOR_2)
    t.circle(100, 100)
    t.right(530)
    
    t.color(COLOR_1)
    t.circle(110, 110)
    t.left(-530)
    
    t.color(COLOR_2)
    t.circle(120, 120)
    t.right(530)
    
screen.exitonclick()
