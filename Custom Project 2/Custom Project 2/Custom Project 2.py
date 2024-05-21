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
base = input("Spacious(1), Tall(2), Fancy(3):")


size=100
pensize = 3

posy = random.randint(-500, 500)
angle = random.randint(0,360)
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
    color1 = "aquamarine"
    color2 = "turquoise"
    color3 = "navy"
    color4 = "blue"
    color5 = "cyan"
    color6 = "medium sea green"
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
    bgcolor = "midnight blue"
    
elif temperature == "3" or temperature == "1":
    bgcolor = color2
    if temperature == "1":
        color2 = "gray"
    elif temperature == "3":
        color2 = "blue violet"
elif temperature == "2":
    bgcolor = color1
    color1 = "White"





if shape == "1":
    def A1_1():
        t.right(180)
        t.penup()
        t.forward(int(size)*0.5)
        t.pendown()
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
            t.forward(int(size)/2)
            t.right(90)
            t.forward(int(size)*1.5)
            t.right(90)
elif shape == "3":
    def A1_1():
        for j in range(3):
            t.forward(size)
            t.right(120)
    def A1_2(): 
        t.forward(int(size)*0.7)
        t.right(75)
        t.forward(int(size)*0.6)
        t.right(45)
        t.forward(int(size)*1.2)
        t.right(120)
        t.forward(int(size)*1.2)
        t.right(45)
        t.forward(int(size)*0.6)
        t.right(75)
        
        
def A1_F1():
    t.begin_fill()
    A1_1()
    t.end_fill()
    
def A1_F2():
    t.begin_fill()
    A1_2()
    t.end_fill()
        


    
turtle.screensize(800,600)
t = turtle.Turtle()
t.speed(25)
s = turtle.Screen()
turtle.bgcolor(bgcolor)
s.title("Custom Project 2")


t.color(color1)
posx = -750
if enviornment == "1":
    
    for k in range(3):
        t.right(240)
        posx += 375
        posy = random.randint(-500, 500)
        size = 250
        t.penup()
        t.goto(posx, posy)
        t.pendown()
        t.begin_fill()
        A1_1()
        t.end_fill()
elif enviornment == "2":
    
    posx = -735
    t.pensize(3)
    for k in range(21):
        t.right(72)
        posx += 70
        posy = random.randint(-500, 500)
        size = 40
        t.penup()
        t.goto(posx, posy)
        t.pendown()
        A1_1()
    t.pensize(1)

elif enviornment == "3":

    t.pendown()
    posx = -770
    for k in range(110):
        t.right(18)
        posx += 14
        posy = random.randint(-500, 500)
        size = 15
        t.penup()
        t.goto(posx, posy)
        t.pendown()
        A1_1()
        
        
        
if terrain == "1":
    posA5 = -200
elif terrain == "2":
    if shape == "1":
        posA5 = -450
    elif shape == "2":
        posA5 = -400
    elif shape == "3":
        posA5 = -500
elif terrain == "3":
    posA5 = -100
    
t.penup()
t.goto(0, posA5)
t.pendown()
t.color(color3)
if base == "1":
    t.setheading(0)
    t.penup()
    t.goto(-225, posA5)
    t.pendown()
    t.begin_fill()
    t.forward(450)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(175)
    t.left(90)
    for q in range(4):
        t.forward(16)
        t.left(90)
        t.forward(16)
        t.right(90)
        t.forward(16)
        t.right(90)
        t.forward(16)
        t.left(90)
    t.forward(16)
    t.left(90)
    t.forward(175)
    t.right(90)
    t.forward(150)
    t.left(90)
    t.forward(75)
    t.end_fill()
    t.penup()
    t.goto(200, int(posA5)+35)
    t.pendown()
    size = 14
    t.color(color2)
    t.pensize(3)
    for r in range(10):
        t.setheading(180)
        A1_1()
        t.penup()
        t.forward(42)
        t.pendown()
    
    t.pensize(1)
    
elif base == "2":
    size = 150
    t.penup()
    t.goto(75, posA5)
    t.pendown()
    t.setheading(180)
    A1_F1()
    t.penup()
    t.goto(35,int(posA5)+150)
    t.pendown()
    A1_F2()
elif base == "3":
    size = 200
    t.penup()
    t.goto(0, posA5)
    t.pendown()
    t.setheading(180)
    A1_F1()
    pensize = 5
    move = 0
    for q in range(4):
        pensize -= 1
        t.pensize(pensize)
        move += 25
        size -= 30
        t.penup()
        t.goto(0-int(int(move)/2),int(posA5)+int(move))
        t.pendown()
        mystery_color = random.choice(mysterycolor)
        t.color(mystery_color)
        A1_1()
    
        
        
if terrain == "1":
    t.setheading(180)
    t.pensize(5)
    for n in range(3):
        posx = random.randint(-800, 800)
        t.color(color6)
        t.penup()
        t.goto(posx, -200)
        t.pendown()
        size =500
        A1_2()
        
    t.pensize(1)
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
    
    
    t.color(color5)
    t.penup()
    t.goto(400,400)
    size=200
    t.pendown()
    #t.begin_fill()
    #A1_1()
    #t.end_fill()
    
    
        

elif terrain == "2":
    t.begin_fill()
    t.penup()
    t.goto(-800, 550)
    t.pendown()
    t.setheading(90)
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
    t.setheading(0)
    t.penup()
    t.goto(-250,-100)
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
    
    size=150
    t.penup()
    t.goto(400,400)
    t.pendown()
    A1_F1()
    
    t.penup()
    t.goto(-600,-300)
    t.pendown()
    A1_F1()
    t.pensize(3)
    
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