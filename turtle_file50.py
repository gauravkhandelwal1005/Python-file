import turtle
import colorsys
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Butterfly Animation")
screen.setup(700, 700)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

i = 0

def animate():
    global i 
    
    if i >= 360:
        i = 0
        t.clear()
        
    hue = i / 360
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    
    angle = math.radians(i)

    x = 180 * math.sin(angle)
    y = 260 * math.sin(angle)*math.cos(angle)
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(x, y)
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(-x, y)
    
    screen.update()
    
    i += 1
    screen.ontimer(animate, 30)
    
animate()
turtle.done()
