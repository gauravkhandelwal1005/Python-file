from turtle import * 
tracer(15)
bgcolor("black")
c = ("#ff66cc", "white")
pensize(3)
for i in range(520):
    color(c[i % 2])
    forward(i)
    right(20)
    for j in range(6):
        forward(j)
        right(145)
        backward(j/2)
        left(180)
done()
        
