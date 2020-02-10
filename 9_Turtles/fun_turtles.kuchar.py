import turtle

# Turtle object
t = turtle.Turtle()
t.screen.bgcolor("green")
t.screen.screensize(500, 500)
t.shape("turtle")
t.color("blue")
t.home()
t.speed(10)

a_stamp = turtle.stamp()

i = 0
while i < 390:
    t.pu()
    t.fd(95)
    t.pd()
    t.pensize(4)
    t.fd(10)
    t.pu()
    t.fd(20)
    t.pd()
    b_stamp = t.stamp()
    t.pu()
    t.home()
    t.right(i); i += 30

t.screen.exitonclick()

