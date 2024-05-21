from turtle import *

clearscreen()
t = Turtle()
bgcolor("black")
speed(1000)
hideturtle()
t.pensize(3)


for i in range(40):
    color("red")
    circle(i*1.3)
    color("orange")
    circle(i)
    color("yellow")
    circle(i*0.8)
    color("green")
    circle(i*0.6)
    color("blue")
    circle(i*0.4)
    color("indigo")
    circle(i*0.2)
    color("purple")
    circle(i*0.1)
       

exitonclick()
 

