import turtle
import colorsys
import math
screen = turtle.Screen()
screen.title("Aesthetic Horphing Plasma Web")
screen.bgcolor("#030008")
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
time = 0
try:
    while True:
        t.clear()
        lines = 180
        factor = 3 + math.sin(time * 0.2) * 2
        for i in range(lines):
            angle = i * (math.pi * 2) / lines
            hue = (angle / (math.pi * 2) + time * 0.1) % 1.0
            color = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
            t.pencolor(color)
            core_radius = 80 + math.sin(time * 2 + angle * 4) * 20
            x1 = math.cos(angle + time) * core_radius
            y1 = math.sin(angle + time) * core_radius
            outer_Radius = 200 + math.cos(time + angle * 3) * 30
            x2 = math.cos(angle * factor) * outer_Radius
            y2 = math.sin(angle * factor) * outer_Radius
            t.pensize(1)
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)
            t.dot(3, "white")
        screen.update()
        time += 0.015
except turtle.Terminator:
    pass
except KeyboardInterrupt:
    pass
