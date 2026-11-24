import turtle, math
t = turtle.Turtle(); t.speed(0)
turtle.Screen().bgcolor("black")
c, s = math.cos, math.sin
def heart(i, n, k):
    a = 6.283 * (i + .5) / n
    x = 16 * s(a) ** 3; z = 24-4*k
    y = 13*c(a)-5*c(2*a)-2*c(3*a)
    t.pu(); t.goto((z-6)*x, (z-6)*y)
    t.color(i/n, k/5, .3+k/6)
    t.pd(); t.seth(140)
    t.begin_fill(); t.fd(z)
    t.circle(-z/2 , 200); t.lt(120)
    t.circle(-z/2, 200); t.fd(z)
    t.end_fill()
for k in range(4):
    for i in range(44 - 10*k):
        heart(i, 44 - 10*k, k)
