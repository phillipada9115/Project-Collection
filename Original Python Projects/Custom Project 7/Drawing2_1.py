from turtle import *
import random

clearscreen()
t = Turtle()
bgcolor("red")
screensize(600, 600)
t.shape("circle")
t.speed(2000)
t.pensize(20)
t.color("lemon chiffon")

color_list = ["orange red", "coral", "Orange", "gold", "khaki",
              "yellow", "sandy brown", "dark orange", "tomato"]

angle = random.randint(0, 360)
t.setheading(angle)

for i in range(50000):
    
    j = i/3
    round(j)
    color = color_list[int(j%9)]
    t.pencolor(color)
    
    t.forward(10)
    
    if abs(int(t.xcor())) >= 400:
        t.left(90)
        t.forward(10)
        if abs(int(t.ycor())) >= 400:
            t.left(60)
            
        
    if abs(int(t.ycor())) >= 400:
        t.left(90)
        t.forward(10)
        if abs(int(t.xcor())) >= 400:
            t.left(60)
            
    
exitonclick()

        
    
