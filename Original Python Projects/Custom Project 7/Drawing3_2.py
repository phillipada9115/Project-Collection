from turtle import *
import random

clearscreen()
t = Turtle()
screensize(400, 400)
bgcolor("white")
t.hideturtle()
t.speed(1000)

for i in range(300):

    size = random.randint(10, 40)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    fill = random.randint(0,  1)
    if y >= 0.01*x**2-200:

        color = "blue4"
        fillcolor = "blue"

    elif y <= 0.004*x**2-350:

        color = "red4"
        fillcolor = "red"

    else:

        color = "yellow4"
        fillcolor = "yellow"

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.pensize(size/10)

    if fill == 0:

        t.begin_fill()
        t.fillcolor(fillcolor)

    else:

        if size > 25:
            t.color(fillcolor)

    t.circle(size)

    if fill == 0:

        t.end_fill()