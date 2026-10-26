import turtle
import random
import math

t = turtle.Turtle()
s = turtle.Screen()
s.setup(800, 700)
s.bgcolor("black")
t.speed()
t.hideturtle()

for i in range(180):
    angle = random.uniform(0, 2 * math.pi)
    radius = random.randint(20, 120)
    
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    t.penup()
    t.goto(x*0.2, y*0.2)
    t.pendown()
    t.color(random.choice(
        ["white",
         "cyan",
         "blue",
         "magenta"]
    ))
    t.goto(x, y)
    
turtle.done()
    
