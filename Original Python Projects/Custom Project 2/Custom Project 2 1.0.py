import time
import turtle
import random





print("Which shape is your favorite?")
time.sleep(0.5)
print("type in th' # inside th' () next to th' answer,")
time.sleep(0.5)
shape=input("Circle(1), Square(2), Triangle(3):")

print("Choose your element.")
time.sleep(0.5)
element=input("Earth(1), Fire(2), Water(3), Air(4):")

print("How warm do u desire th' atmosphere to be")
time.sleep(0.5)
temperature = input("Dawn(1), Day(2), Dusk(3), Night(4):")

print("Are you bored or stressed, which is th' best enviornment?")
time.sleep(0.5)
enviornment = input("Peaceful(1), Civil(2), Mania(3):")

print("What realm is best?")
time.sleep(0.5)
terrain = input("Forest(1), basin(2), archeplago(3):")
time.sleep(0.5)

print("U need some shelter?")
time.sleep(0.5)
print("choose a layout for your home?")
time.sleep(0.5)
base = ("Spacious(1), Tall(2), Fancy(3):")


size=100
pensize = 3
posx = random.randint(-800, 800)
posy = random.randint(-600, 600)
size2=100




    

if element == "1":
    color1 = "burlywood"
    color2 = "bisque"
    color3 = "rosybrown"
    color4 = "peru"
    color5 = "sienna"
    color6 = "dark green"
elif element == "2":
    color1 = "crimson"
    color2 = "orange"
    color3 = "firebrick"
    color4 = "red"
    color5 = "darkorange"
    color6 = "deep pink"
elif element == "3":
    color1 = "aqua"
    color2 = "aquamarine"
    color3 = "navy"
    color4 = "blue"
    color5 = "doger blue"
    color6 = "lime"
elif element == "4":
    color1 = "lavenderblush"
    color2 = "lavender"
    color3 = "lightgrey"
    color4 = "medium orchid"
    color5 = "gainsboro"
    color6 = "gold"

mysterycolor = [color1, color2, color3, color4, color5, color6]    
mystery_color = random.choice(mysterycolor)

    
if temperature == "4":
    bgcolor = "black"
    
elif temperature == "3" or temperature == "2":
    bgcolor = "sky blue"
elif temperature == "1":
    bgcolor = color1
    color1 = "White"





if shape == "1":
    def A1_1():
        t.right(180)
        t.circle(size)
        t.right(180)
    def A1_2():
        for i in range(2):
            t.forward(int(size2)*0.7)
            t.right(60)
            for j in range(20):
                t.forward(int(size2)/20)
                t.right(3)
            t.right(60)
elif shape == "2":
    def A1_1():
        for i in range(4):
            t.forward(size)
            t.right(90)
    def A1_2():
        for i in range(2):
            t.forward(int(size2)/2)
            t.right(90)
            t.forward(int(size2)*1.5)
            t.right(90)
elif shape == "3":
    def A1_1():
        for j in range(3):
            t.forward(size)
            t.right(120)
    def A1_2(): 
        t.forward(int(size2)*0.7)
        t.right(75)
        t.forward(int(size2)*0.6)
        t.right(45)
        t.forward(int(size2)*1.2)
        t.right(120)
        t.forward(int(size2)*1.2)
        t.right(45)
        t.forward(int(size2)*0.6)
        t.right(75)
        


    
turtle.screensize(800,600)
t = turtle.Turtle()
t.speed(25)
s = turtle.Screen()
turtle.bgcolor(bgcolor)
s.title("Custom Project 2")


if enviornment == "1":
    t.color(color3)    
    A1_1()
    size = int(size)/2
    t.color(color2)
    t.begin_fill()
    A1_1()
    t.end_fill()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    for k in range(5):
        size = 25
        t.color(color4)
        t.begin_fill()
        A1_1()
        t.end_fill()
        t.penup()
        t.left(60)
        t.forward(40)
        t.pendown()
        A1_1()
        t.right(120)
        t.penup()
        t.forward(40)
        t.pendown()
        t.left(60)
elif enviornment == "2":
    for k in range(3):
        t.color(color3)    
        A1_1()
        t.right(120)
    
    
    size = int(size)/2
    t.color(color2)
    
    for l in range(6):
        t.begin_fill()
        A1_1()
        t.end_fill()
        t.penup()
        t.left(60)
        t.forward(50)
        t.pendown()
        size += 10
elif enviornment == "3":
    t.goto(300,300)
    for k in range(6):
        for l in range(3):
            t.color(color1)    
            A1_1()
            t.right(120)
            size += 5
        t.right(120)
        t.forward(100)
    for m in range(3):
        size = 40
        for n in range(10):
            t.begin_fill()
            A1_1()
            t.end_fill()
            t.penup()
            t.left(36)
            t.forward(50)
            t.pendown()
            pensize = pensize + 1
            t.pensize(pensize)
            size += 10
        t.right(120)
        t.forward(100)
        
        
if terrain == "1":
    t.right(180)
    for n in range(3):
        t.color(color5)
        t.penup()
        t.goto(posx, -200)
        t.pendown()
        size =500
        t.begin_fill()
        A1_2()
        t.end_fill()
        posx = random.randint(-800, 800)
    t.penup()
    t.goto(1000, -800)
    t.pendown()
    t.color(color4)
    t.begin_fill()
    for m in range(2):
        t.forward(2000)
        t.right(90)
        t.forward(600)
        t.right(90)
    t.penup()
    t.end_fill()
    t.left(180)
    
        

elif terrain == "2":
    t.begin_fill()
    t.penup()
    t.goto(-800, 550)
    t.pendown()
    t.right(270)
    if shape == "1":
        t.right(140)
        for o in range(30):
            t.right(1)
            t.forward(35)
        t.left(75)
        t.forward(600)
        t.left(90)
        for p in range(30):
            t.right(1)
            t.forward(18)
        t.left(45)
        for q in range(60):
            t.right(1)
            t.forward(10)
        t.right(45)
        t.forward(500)
        

        
    elif shape == "2":
        t.right(180)
        t.forward(750)
        t.left(90)
        t.forward(250)
        t.right(90)
        t.forward(250)
        t.left(90)
        t.forward(250)
        t.left(90)
        t.forward(5)
        t.right(90)
        t.forward(150)
        t.left(90)
        t.forward(45)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(550)
        t.right(90)
        t.forward(600)
        
    elif shape == "3":
        t.right(165)
        t.forward(1000)
        t.left(90)
        t.forward(300)
        t.right(60)
        t.forward(100)
        t.left(50)
        t.forward(300)
        t.left(90)
        t.forward(400)
        t.right(120)
        t.forward(150)
        t.left(90)
        t.forward(350)
        t.left(30)
        t.forward(150)
        t.right(95)
        t.forward(600)
        
    for r in range(3):
            t.right(90)
            t.forward(2000)    
    t.forward(500)
    t.goto(-800, 550)
    t.end_fill()
elif terrain == "3":
    t.color(color4)
    t.penup()
    t.goto(-300,-100)
    t.pendown()
    t.begin_fill()
    t.forward(500)
    t.right(135)
    t.forward(353)
    t.right(90)
    t.forward(353)
    t.end_fill()
    t.right(135)

    t.penup()
    t.goto(400,-200)
    t.pendown()
    t.begin_fill()
    t.forward(200)
    t.right(135)
    t.forward(141)
    t.right(90)
    t.forward(141)
    t.end_fill()
    t.right(135)

    t.penup()
    t.goto(-600,400)
    t.pendown()
    t.begin_fill()
    t.forward(150)
    t.right(120)
    t.forward(50)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.forward(50)
    t.end_fill()
    t.left(60)
    
    for k in range(2):
        size = random.randint(20,100)
        t.color(color6)
        t.penup()
        t.goto(random.randint(-200, 100), -100)
        t.pendown()
        A1_1()
        size = random.randint(20,100)
        t.penup()
        t.goto(random.randint(-200, 100), -100)
        t.pendown()
        A1_2()
    
        
        

s.exitonclick()