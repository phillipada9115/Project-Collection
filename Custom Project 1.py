import turtle
import random
import time


turtle.screensize(800,800)
t=turtle.Turtle()
turtle.bgcolor('black')
t.speed(10)


color1=['pink','lightpink','lightcoral','navajowhite']
color2=['hotpink','lightsalmon','orange','red']
color3=['crimson','maroon','orangered','deeppink']
color4=['lightyellow','cornsilk','honeydew','greenyellow']
color5=['yellow','lime','khaki','springgreen']
color6=['gold','green','olive','mediumseagreen']
color7=['lightcyan','aquamarine','lavender','powderblue']
color8=['deepskyblue','cyan','mediumslateblue','magenta']
color9=['steelblue','indigo','navy','purple']


for i in range(1000):
    posx=random.randint(-600,600)
    posy=random.randint(-600,600)
    size=random.randint(20,200)
    angle=random.randint(-90,90)
    selection=random.randint(0,4)
    
    if size<=110:
        selection2=0
    else:
        selection2=1
    
    t.penup()
    t.goto(posx,posy)
    t.pendown()
    t.left(angle)
    
    if t.xcor()<=-200: 
        if t.ycor()<=-200:
            color=random.choice(color3)
        elif t.ycor()>=200:
            color=random.choice(color1)
        else:
            color=random.choice(color2)
    elif t.xcor()>200:
        if t.ycor()<=-200:
            color=random.choice(color9)
        elif t.ycor()>=200:
            color=random.choice(color7)
        else:
            color=random.choice(color8)
    else:
        if t.ycor()<=-200:
            color=random.choice(color6)
        elif t.ycor()>=200:
            color=random.choice(color4)
        else:
            color=random.choice(color5)
        
        
    
    if selection2==0:
        t.begin_fill()
    t.color(color)
        
        
    if selection==0:
        t.circle(size)
    elif selection==1:
        for j in range(4):
            t.forward(size)
            t.left(90)
    elif selection==2:
        for k in range(3):
            t.forward(size)
            t.left(120)
    elif selection==3:
        for l in range(6):
            t.forward(int(size)/1.75)
            t.left(60)
    else:
        for l in range(5):
            t.forward(int(size)/1.75)
            t.right(144)
            t.forward(int(size)/1.75)
            t.left(72)
            
    if selection2==0:
        t.end_fill()
    

    
        
time.sleep(60)




