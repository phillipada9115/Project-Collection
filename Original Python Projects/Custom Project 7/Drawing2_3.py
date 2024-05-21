from turtle import *
import random

clearscreen()
t = Turtle()
bgcolor("blue")
screensize(400, 400)
t.speed(5000)
t.hideturtle()

colors_list = ["spring green", "aquamarine", "cyan", "steel blue",
               "navy", "indigo"]

for i in range(200):
    pensize = random.randint(1, 5)
    t.pensize(pensize)
    j = random.randint(3, 20)/5
    k = random.randint(30, 120)
    direction = random.randint(0, 1)
    m = random.randint(0, 360)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = random.choice(colors_list)
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(m)
    t.color(color)
    
    t.circle(k*j, k)

exitonclick()

