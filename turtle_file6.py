import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My turtle window")
screen.setup(width= 700, height=500)
t= turtle.Turtle()
t.shape("turtle")
t.color("darkblue")
t.forward(150)
screen.exitonclick()
