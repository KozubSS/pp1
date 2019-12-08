import turtle

pen = turtle.Turtle()

for x in range(8):
    if x % 2 == 0:
        pen.forward(100)
    else:
        pen.right(90)     

turtle.done()