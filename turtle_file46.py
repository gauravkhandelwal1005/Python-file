import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
for i in range(5):
    a = 60 + i * 15
    t.pu(); t.goto(0, -300)
    t.seth(a); t.pd(); t.width(8)
    t.color("limegreen"); t.fd(520)
    p = t.pos(); t.width(2)
    for k in range(120):
        r = 150 - k // 3 * 3.5
        t.color(1, k / 140, i / 5)
        t.seth(a - 60 + k % 3 * 20)
        t.circle(r, 80); t.lt(100)
        t.circle(r, 80); t.goto(p)
