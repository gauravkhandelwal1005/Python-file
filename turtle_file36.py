import turtle
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
for i in range(30):
    t.color("darkorange", "gold")
    t.begin_fill()
    t.setheading(i * 12)
    t.circle(300, 60); t.left(120)
    t.circle(300, 60)
    t.end_fill()
t.penup()
for i in range(800):
    t.home(); t.left(i * 137.508)
    t.forward(6.5 * i ** 0.5)
    v = 0.25 + i / 1400
    t.dot(15, (v, v / 2.2, 0))
