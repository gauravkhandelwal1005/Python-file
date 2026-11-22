import turtle, colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
t.pensize(2)
for i in range(180):
        h = (i / 90 + i % 3 / 3) % 1
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.pencolor(c)
        r = 280 - i % 3 * 80
        for _ in range(2):
                t.circle(r, 60)
                t.left(120)
        if i % 3 == 2:
                t.left(6)
t.dot(40, "white")
turtle.done()
