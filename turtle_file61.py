import turtle
s = turtle.Screen()
s.setup(width = 1.0, height = 1.0)
s.title("Raindow Neon Spiral")
s.bgcolor("black")
s.tracer(3)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = [
    "#001F3F",
    "#002B5B",
    "#003366",
    "#0047AB",
    "#005F73",
    "#006D77",
    "#008B8B",
    "#20B2AA"
]

for i in range(700):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 0.8)
    t.left(137)
    t.forward(i * 0.5)
    t.left(143)
turtle.done()
