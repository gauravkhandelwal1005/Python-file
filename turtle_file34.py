import turtle

screen = turtle.Screen()
screen.setup(width = 800, height = 800)
screen.title("Advanced Spiraling Star Mesh")

pen = turtle.Turtle()
pen.shape("arrow")
pen.color("green")
pen.speed(0)
pen.pensize(2)

colors = ["#c8102e", "#006738", "#4a0d0d"]
pen.penup()
pen.goto(-150, 50)
pen.pendown()

for i in range(100):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 5)
    pen.right(144)
turtle.done()
