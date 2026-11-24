import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.width(2)
colors = ["cyan", "spring green", "lime", "turquoise"]

for i in range(90):
    t.color(colors[i % len(colors)])
    t.circle(120, 75)
    t.left(105)
    t.circle(120, 75)
    t.left(40)
    
turtle.done()
