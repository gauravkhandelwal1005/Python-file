import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pencolor("cyan")
t.hideturtle()
for i in range(240):
  t.forward(i*3)
  t.left(89)
  t.circle(30)
  t.left(94)
turtle.done()
