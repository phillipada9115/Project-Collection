from tkinter import *
from tkinter import Tk
import random


root = Tk()
root.title("Custom Project 3")
root.geometry("1000x700+150+150")


canvas = Canvas(root, width = 320, height = 320, bg = "blue")
canvas.pack()

canvas2 = Canvas(root, width = 250, height = 250, bg = "yellow")
canvas2.place(x = 650, y = 700)

canvas3 = Canvas(root, width = 500, height = 500, bg = "red")
canvas3.place(x = 1100, y = 100)


posx = 0
posy = 0
bank = 0
def createsquare():
    global posx
    global posy 
    global bank
    canvas.create_rectangle(posx, posy, posx+40, posy+40, fill = "purple", outline = "blue")
    if posx >= 280:
        posx = -40
        posy +=40
        if posy >= 280:
            posy -= 275
            turquoise.configure(text = "Too purple!")
    posx +=40
    bank += 1
    
def createcircle():
    global bank
    posx2 = random.randint(40,210)
    posy2 = random.randint(40,210)
    canvas2.create_oval(posx2-20, posy2-20, posx2+20, posy2+20, fill = "yellow", outline = "green", width = 3)
    bank +=1
    
    
def createtriangles():
    global bank
    posx3 = random.randint(40,460)
    posy3 = random.randint(40,460)
    global posx
    global posy 
    canvas3.create_polygon(posx3, posy3, 250, 250, posx3+40, posy3, fill = "red", outline = "orange", width = 3)
    bank += 1

    
def changenumber1():
    global numbertext1
    selection1 = random.randint(0,4)
    if selection1 == 0:
        numbertext1 /= 8
    else:
        numbertext1 *= 2
        
    if numbertext1 > 10000:
        numbertext1 = 10
        turquoise.configure(text= "No, no, no!")
        
    round(numbertext1, -3)
    
    number1.configure(text = str(numbertext1))


def changenumber2():
    global numbertext2
    numbertext2 += 1
    number2.configure(text = str(numbertext2))


def changenumber3():
    global numbertext3
    selection3 = random.randint(0,4)
    if selection3 == 0:
        numbertext3 += 5
    else:
        numbertext3 -= 1
    number3.configure(text = str(numbertext3))
    
    
fonts = ["Times New Roman", "Arial", "Courier New", "Verdana", "Comic Sans MS", "MS Sans Serif", "MS Serif"]
def lavender():
    lavfonts = random.choice(fonts)
    number1.configure(font = (lavfonts, 50))
    number2.configure(font = (lavfonts, 50))
    number3.configure(font = (lavfonts, 50))
    pinklabel.configure(font = (lavfonts, 50))
    pinklabel2.configure(font = (lavfonts, 50))
    turquoise.configure(font = (lavfonts, 50))
    
def lime():
    global bank
    posx4 = random.randint(0,280)
    posy4 = random.randint(0,280)
    canvas.create_rectangle(posx4, posy4, posx4+20, posy4+20, fill = "lime", outline = "white")
    posx2 = random.randint(40,210)
    posy2 = random.randint(40,210)
    canvas2.create_oval(posx2-20, posy2-20, posx2+20, posy2+20, fill = "lime", outline = "white", width = 8)
    posx3 = random.randint(40,460)
    posy3 = random.randint(40,460)
    canvas3.create_polygon(posx3, posy3, 250, 250, posx3+50, posy3, fill = "lime", outline = "white", width = 2)
    turquoise.configure(text = "Slime, more slime.")
    bank += 3
    
def pink():
    global bank
    tot = numbertext1 + numbertext2 + numbertext3
    number1.configure(text = 10)
    number2.configure(text = 0)
    number3.configure(text = 10)
    
    
    canvas.delete('all')
    canvas2.delete('all')
    canvas3.delete('all')
    
    pinklabel.configure(text = "Total: "+str(tot))
    pinklabel2.configure(text = "Bank: "+str(bank))
    turquoise.configure(text = "nice statz!")
    
    bank = 0
    display_pallete()
    
    


numbertext1 = 10
number1 = Label(root, text ="10", fg = "purple", font = ("Times New Roman", "50"))
number1.place(x=650, y = 350)  

numbertext2 = 0
number2 = Label(root, text ="0", fg = "green", font = ("Times New Roman", "50"))
number2.place(x=650, y = 450) 

numbertext3 = 10
number3 = Label(root, text ="10", fg = "orange", font = ("Times New Roman", "50"))
number3.place(x=650, y = 550)   

limelabel = Label(root, text ="", fg = "lime") 

pinklabel = Label(root, text ="", fg = "pink",font = ("Times New Roman", "50"))
pinklabel.place(x = 1100, y = 700)

pinklabel2 = Label(root, text ="", fg = "pink", font = ("Times New Roman", "50"))
pinklabel2.place(x = 1100, y = 800)

turquoise = Label(root, text ="", fg = "turquoise1", font = ("Times New Roman", "50"))
turquoise.place(x = 1100, y = 0)


Button(root, width = 15, height = 15, fg = "blue", bg= "purple", command = changenumber1).place(x = 100, y = 50)
Button(root, width = 15, height = 15, fg = "blue", bg= "green", command = changenumber2).place(x = 300, y = 50)
Button(root, width = 15, height = 15, fg = "blue", bg= "orange", command = changenumber3).place(x = 500, y = 50)
Button(root, width = 15, height = 15, fg = "blue", bg= "blue", command = createsquare).place(x = 100, y = 300)
Button(root, width = 15, height = 15, fg = "blue", bg= "yellow", command = createcircle).place(x = 300, y = 300)
Button(root, width = 15, height = 15, fg = "blue", bg= "red", command = createtriangles).place(x = 500, y = 300)
Button(root, width = 15, height = 15, fg = "blue", bg= "lavender", command = lavender).place(x = 100, y = 550)
Button(root, width = 15, height = 15, fg = "blue", bg= "lime", command = lime).place(x = 300, y = 550)
Button(root, width = 15, height = 15, fg = "blue", bg= "pink", command = pink).place(x = 500, y = 550)









root.mainloop()