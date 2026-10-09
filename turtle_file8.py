import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
for i in range(50):
    angle = random.randint(0, 360)
    distance = random.randint(10, 50)
    t.setheading(angle)
    t.forward(distance)
screen.exitonclick()
