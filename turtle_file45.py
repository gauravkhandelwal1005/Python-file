import turtle, colorsys as cs
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
t.pensize(2)
for k in range(6):
    r = 320 - k * 48
    s = 0.25 + k * 0.13
    c = cs.hsv_to_rgb(.93, s, 1)
    t.color("hot pink", c)
    for i in range(12):
        t.setheading(i*30 + k*15)
        t.begin_fill()
        for _ in range(2):
            t.circle(r, 60)
            t.left(120)
        t.end_fill()
t.dot(50, "gold")
turtle.done()
