import turtle, math, colorsys as cs
t = turtle.Turtle(); t.speed(0)
turtle.bgcolor("black")
def go(x, y):
    t.goto(x*.94 - y*.34, x*.34 + y*.94)
def ring(a0, a1):
    for r in range(250, 420, 9):
        t.width(3); t.penup()
        t.pencolor(cs.hsv_to_rgb(r/200, .7, 1))
        for a in range(a0, a1 + 1, 3):
            g = math.radians(a)
            go(r*math.cos(g), r*math.sin(g)*.3)
            t.pendown()
ring(0, 180)
for y in range(-180, 181, 3):
    w = (180**2 - y**2) ** .5
    t.width(3); t.penup(); go(-w, y)
    t.pencolor(cs.hsv_to_rgb(.08+y/3000, .7, 1))
    t.pendown(); go(w, y)
ring(180, 360)
