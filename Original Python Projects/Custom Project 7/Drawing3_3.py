from turtle import *
import random

clearscreen()
t = Turtle()
screensize(-300, 300)
bgcolor("white")
t.speed(20)


colornum = 0
pensize = 1
color_list = ["orange", "dark orange", "orange red", "red", "crimson",
              "deep pink", "medium violet red", "purple", "violet", "magenta",
              "pink","tomato", "sandy brown"]
t.penup()
t.goto(-400, -375)
t.pendown()

for i in range(3):
    t.setheading(9)

    for j in range(41):

        colornum += 1

        if j % 4 == 0:
            pensize += 1

        color = color_list[colornum % 11]
        t.pensize(pensize)
        t.color(color)
        t.pencolor(color)
        t.forward(20)

    t.setheading(171)
    for j in range(41):
        colornum += 1
        if j % 4 == 0:
            pensize += 1
        color = color_list[colornum % 9]
        t.pensize(pensize)
        t.color(color)
        t.pencolor(color)
        t.forward(20)
        

pensize = 1
color_list2 = ["red", "crimson","deep pink", "medium violet red", "purple", 
              "indigo", "navy", "blue", "slate blue", "medium purple",
              "violet", "magenta", "pink"]
t.penup()
t.goto(400, 375)
t.pendown()
for i in range(3):
    t.setheading(189)

    for j in range(41):

        colornum += 1

        if j % 4 == 0:
            pensize += 1

        color = color_list2[colornum % 11]
        t.pensize(pensize)
        t.color(color)
        t.pencolor(color)
        t.forward(20)

    t.setheading(351)
    for j in range(41):
        colornum += 1
        if j % 4 == 0:
            pensize += 1
        color = color_list2[colornum % 9]
        t.pensize(pensize)
        t.color(color)
        t.pencolor(color)
        t.forward(20)
        
exitonclick()