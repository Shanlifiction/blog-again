import turtle

t1 = turtle.Turtle()
t1.pensize(3)
colors = ["red", "blue", "green", "orange", "purple"]
radius = 30
for color in colors:
    t1.color(color)
    t1.circle(radius)
    t1.penup()
    t1.right(90)
    t1.forward(20)
    t1.left(90)
    t1.pendown()
    radius += 20

turtle.done()