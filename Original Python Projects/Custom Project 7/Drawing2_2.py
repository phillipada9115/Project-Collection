from turtle import *
import random 

clearscreen()
t = Turtle()
bgcolor("Yellow")
screensize(400, 400)
t.speed(1000)

color_list = ["black", "black", "gray10", "darkgoldenrod4",
              "goldenrod4", "gold4", "gold3", "gold2", "gold1", "gold"]

for i in range(50):

    pensize = 1
    t.pensize(pensize)
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x,y)
    t.pendown()
    j = random.randint(3, 10)

    for k in range(j):
        
        color = color_list[k-1]
        t.color(color)
        pensize += 1
        t.pensize(pensize)
        t.penup()
        t.setheading(270)
        t.forward(15)
        t.pendown()
        t.setheading(0)
        t.circle(15*k)
        
exitonclick()
