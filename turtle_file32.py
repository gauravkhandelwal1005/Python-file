import turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0.5)

colors = ["red", "orange", "yellow",
    "green", "blue", "indigo", "violet"]

for j in range(36):
    t.color(colors[j % 7])
    t.left(10)
    for i in range(5):
        t.forward(100)
        t.right(144)
        
screen.mainloop()
