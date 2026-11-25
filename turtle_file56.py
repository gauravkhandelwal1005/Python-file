import turtle, random
import colorsys

random.seed(7)
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
for i in range(3000):
    r = random.random() ** 1.4 * 450
    a = i % 3 * 120 + r * 0.7
    a += random.gauss(0, 16)
    t.goto(0, 0)
    t.setheading(a)
    t.forward(r)
    h, s = 0.55 + r / 1100, r / 450
    c = colorsys.hsv_to_rgb(h, s, 1)
    t.dot(random.randint(2, 7), c)
    
screen.update()
turtle.done()
