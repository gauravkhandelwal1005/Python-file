import turtle, math, colorsys
turtle.bgcolor("black")
hsv = colorsys.hsv_to_rgb
a, b, r = [turtle.Turtle() for _ in range(3)]
for p in (a, b, r):
    p.speed(0); p.width(5); p.penup()
r.width(3)
for i in range(181):
    x = i * 4 - 360
    y = 170 * math.sin(i / 14)
    a.pencolor(hsv(i / 180, 1, 1))
    b.pencolor(hsv(i / 180 + .5, 1, 1))
    a.goto(x, y); b.goto(x, -y)
    a.pendown(); b.pendown()
    if i % 6 == 0:
        r.goto(x, y); r.pendown()
        r.pencolor(a.pencolor()); r.goto(x, 0)
        r.pencolor(b.pencolor()); r.goto(x, -y)
        r.penup(); a.dot(14); b.dot(14)
turtle.done()
