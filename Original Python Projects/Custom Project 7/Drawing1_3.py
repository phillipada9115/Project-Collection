from turtle import *
import random

clearscreen()
t = Turtle()
bgcolor("black")
screensize(600,600)
t.speed(100)

color_list = ["pink", "hotpink", "deeppink",
              "purple", "dark magenta", "violet", "magenta"]

t.hideturtle()
t.penup()
t.goto(100, 100)
t.pendown()

for i in range(36):
    
    j = 200-5*i
    color = color_list[i%7]
    number = random.randint(1, 10)
    t.pencolor(color)
    t.fillcolor(color)
    if i % 2 == 1:
        t.begin_fill()
        
    for k in range(5):
        
        t.forward(j)
        t.right(126)
        t.forward(j)
        t.left(54)
        
    if i % 2 == 1:
        t.end_fill()

    t.right(number)
    
exitonclick()
