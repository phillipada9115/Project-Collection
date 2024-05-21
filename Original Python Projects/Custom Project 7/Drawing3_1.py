from turtle import *
import random


clearscreen()
t = Turtle()
bgcolor("white")
screensize(400,400)
t.shape("square")
t.hideturtle()


color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


for i in range (150):
    color = random.choice(color_list)
    t.color(color)
    t.pencolor(color)
    t.speed(2)
    
    if t.xcor() > 200:
        t.setheading(random.randint(120, 240))
    elif t.xcor() < -200:
        t.setheading(random.randint(300, 420))
    elif t.ycor() > 200:
        t.setheading(random.randint(220, 330))
    elif t.ycor() < -200:
        t.setheading(random.randint(30, 150))
    else:
        t.setheading(random.randint(0,360))
    t.penup()
    t.showturtle()
    t.forward(random.randint(20,200))
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.hideturtle()
    t.speed(100)
    for j in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()
    

exitonclick()