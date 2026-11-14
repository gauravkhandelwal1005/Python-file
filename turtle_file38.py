import turtle, math, colorsys
hsv = colorsys.hsv_to_rgb
t = turtle.Turtle(); t.speed(0)
turtle.Screen().bgcolor("black")
t.width(2)
def heart(k, s):
    c = math.cos
    y = 13*c(k) - 5*c(2*k) - 2*c(3*k)
    y = y - c(4*k)
    return 16*math.sin(k)**3*s, y*s
for n in range(30):
    t.pu()
    t.color(hsv(.8+n/150, 1, 1))
    for i in range(127):
        t.goto(heart(i/20, 3+n))
        t.pd()

t.hideturtle()
turtle.done()
