from turtle import *

bgcolor("black")
pu()
setpos(170, -170)
pd()
width(4)
speed(15)

R = 1
G = 1
B = 0


for i in range(150):
    begin_fill()
    color((R, G, B))
    circle(140 - i, 50)
    lt(80)
    circle(130 - i, 50)
    rt(150)
    R -= 0.0065
    G -= 0.0065
    
    end_fill()
done()
