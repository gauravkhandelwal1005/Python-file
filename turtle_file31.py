import turtle
import colorsys
import random

random.seed(11)

screen = turtle.Screen()
screen.setup(800, 480)
screen.bgcolor("#07040f")
screen.colormode(1.0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1.3)

def glow(h):
    return colorsys.hsv_to_rgb(h % 1, 0.72, 1.0)

def stars():
    t.penup()
    for _ in range(90):
        x = random.randint(-390, 390)
        y = random.randint(-230, 230)
        t.goto(x, y)
        t.dot(random.randint(2, 4), "white")
        
def petal(size, hue):
    t.pencolor(glow(hue))
    t.pendown()
    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
    t.penup()
    
def ring(count, size, hue, shift):
    for i in range(count):
        t.goto(0, 0)
        t.setheading(i * 360 / count + shift)
        petal(size, hue + i / count * 0.4)
        
def spiral():
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    for i in range(150):
        t.pencolor(glow(0.55 + i / 150))
        t.forward(2 + i * 0.35)
        t.left(59)
    t.penup()
    
stars()
ring(40, 215, 0.55, 0)
ring(32, 165, 0.72, 5)
ring(24, 120, 0.90, 0)
ring(18, 80, 0.07, 10)
ring(12, 46, 0.14, 0)
spiral()
t.goto(0, 0)
t.dot(14, "#fff3c4")
turtle.done()
