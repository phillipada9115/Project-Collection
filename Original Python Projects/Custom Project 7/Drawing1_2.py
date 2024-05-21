from turtle import *
import random

clearscreen()
t = Turtle()
bgcolor("black")
t.hideturtle()
t.pendown()
t.speed(1000)
color_list = ["cyan", "turquoise", "teal", "blue", "navy", "indigo", "violet"]
    



for i in range(500):
    t.pensize(1+(i/5))
    color = random.choice(color_list)
    k = random.randint(850, 950)
    l = k/10
    t.pencolor(color)
    t.forward(i)
    t.left(l)
    
exitonclick()
