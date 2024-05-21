import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
import random

#work on 2 more levels, & other things

root = Tk()
root.geometry("500x500")
root.title("Custom Project 9")
root.configure(bg = "blue")

treasure_x = random.randint(1, 9)
treasure_y = random.randint(1, 9)
lives = 3
treasure = 0


def treasuremap1():
    x, y = np.meshgrid(np.linspace(0, 10, 256), np.linspace(0, 10, 256))
    z = np.sqrt((x - treasure_x)**2 + (y - treasure_y)**2)
    fig, ax = plt.subplots()
    ax.contourf(x, y, z, cmap = "plasma")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
def treasuremap2():
    x, y = np.meshgrid(np.linspace(0, 10, 256), np.linspace(0, 10, 256))
    z = np.cos(np.sqrt((x - treasure_x)**2 + (y - treasure_y)**2 )+np.sqrt(x**2 + y**2))
    fig, ax = plt.subplots()
    ax.contourf(x, y, z, cmap = "inferno")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
def treasuremap3():
    x, y = np.meshgrid(np.linspace(0, 10, 256), np.linspace(0, 10, 256))
    z = (np.sqrt(np.abs((x - treasure_x)**2) + np.abs((y - treasure_y)**2) )-np.sqrt((x - 0.5)**2 + (y - 0.5)**2)
         -np.sqrt((x -9.5)**2 + (y - 9.5)**2)-np.sqrt((x - 0.5)**2 + (y - 9.5)**2)-np.sqrt((x - 9.5)**2 + (y - 0.5)**2))
    
    fig, ax = plt.subplots()
    ax.contourf(x, y, z, levels = np.linspace(z.min(), z.max(), 20), cmap = "cividis")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
def treasuremap4():
    x, y = np.meshgrid(np.linspace(0, 10, 256), np.linspace(0, 10, 256))
    z = (np.sqrt((x - treasure_x)**2 + (y - treasure_y)**2 )-np.sqrt(x**2 + y**2)
         -np.sqrt((x-10)**2 + (y)**2))
    
    fig, ax = plt.subplots()
    
    ax.contourf(x, y, z, levels = np.linspace(z.min(), z.max(), 20), cmap = "bone")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
def treasuremap5():
    x, y = np.meshgrid(np.linspace(0, 10, 256), np.linspace(0, 10, 256))
    z  = ((1/np.sqrt(np.abs(x - 2.5)+np.abs(y - 2.5)))+
          (1/np.sqrt(np.abs(x - 7.5)+np.abs(y - 2.5)))+
          (1/np.sqrt(np.abs(x - 2.5)+np.abs(y - 7.5)))+
          (1/np.sqrt(np.abs(x - 7.5)+np.abs(y - 7.5)))+
          np.sqrt(np.abs(x - treasure_x) + np.abs(y - treasure_y)))
    
    fig, ax = plt.subplots()
    
    ax.contourf(x, y, z, levels = np.linspace(z.min(), z.max(), 50), cmap = "brg")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
         

label1 = Label(root, text="King Φ's Treasure game", bg="blue", fg="white", font = "Calibri 30")
label1.place(x = 10, y = 10)

label4 = Label(root, text="", bg="blue", fg="white", font = "Calibri 30")
label4.place(x = 10, y = 410)

canvas1 = Canvas(root, width = 300, height = 300, bg = "indigo")
canvas1.place(x = 100, y = 100)

button1 = Button(canvas1, text = "Show Map", fg = "purple", bg = "navy", font="Calibri 15", width = 12, height = 3, command = treasuremap1)
button1.place(x = 160, y = 200)

label2 =Label(canvas1, text = "X:", bg = "indigo", fg = "white", font = "Calibri 15")
label2.place(x= 5, y = 5)
Xstring = StringVar()
Xanswer = ttk.Combobox(canvas1, width = 5, textvariable = Xstring, state = "readonly")
Xanswer["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
Xanswer.place(x = 25, y = 10)
Xanswer.current(0)

label3 =Label(canvas1, text = "Y:", bg = "indigo", fg = "white", font = "Calibri 15")
label3.place(x= 5, y = 30)
Ystring = StringVar()
Yanswer = ttk.Combobox(canvas1, width = 5, textvariable = Ystring, state = "readonly")
Yanswer["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
Yanswer.place(x = 25, y = 35)
Yanswer.current(0)

label5 =Label(canvas1, text = "Treasure:"+ str(treasure), bg = "indigo", fg = "white", font = "Calibri 40")
label5.place(x= 5, y = 120)
label6 =Label(canvas1, text = "Lives:"+ str(lives), bg = "indigo", fg = "white", font = "Calibri 40")
label6.place(x= 5, y = 60)

canvas1.create_polygon(225, 115, 160, 50, 190, 20, 260, 20, 290, 50, fill="cyan", outline="white", width=3)
canvas1.create_line(160, 50, 290, 50, fill="white", width=3)
canvas1.create_line(225, 115, 185, 50, 205, 20, fill="white", width=3)
canvas1.create_line(225, 115, 210, 50, 217, 20, fill="white", width=3)
canvas1.create_line(225, 115, 240, 50, 233, 20,fill="white", width=3)
canvas1.create_line(225, 115, 265, 50, 245, 20, fill="white", width=3)


#treasuremap5()

def leave():
    root.destroy()


def dig():
    global treasure, lives, treasure_x, treasure_y
    if Xstring.get() == str(treasure_x) and Ystring.get() == str(treasure_y):
        plt.close("all")
        treasure_x = random.randint(1, 9)
        treasure_y = random.randint(1, 9)
        treasure += 1
        label5.configure(text = "Treasure:" + str(treasure))
        if treasure == 1:
            label4.configure(text = "U found treasure!")
            button1.configure(command = treasuremap2)
        
        elif treasure == 2:
            label4.configure(text = "Found more treasure!")
            button1.configure(command = treasuremap3)
            
        elif treasure == 3:
            label4.configure(text = "Lots of treasure!")
            button1.configure(command = treasuremap4)
        
        elif treasure == 4:
            label4.configure(text = "Treasure is everywhere!")
            button1.configure(command = treasuremap5)
            
        elif treasure == 5:
            canvas1.destroy()
            label4.configure(text = "")
            treasure += lives-1
            canvas2 = Canvas(root, width = 300, height = 300, bg = "indigo")
            canvas2.place(x = 100, y = 100)
            label7 = Label(canvas2, text = "U WIN!", font = ("Calibri", 40), fg = "white", bg = "indigo")
            label7.place(x = 75, y = 25)
            label8 = Label(canvas2, text = str(treasure) + " treasure!", font = ("Calibri", 40), fg = "white", bg = "indigo")
            label8.place(x = 35, y = 100)
            button3 = Button(canvas2, text = "Exit", fg = "purple", bg = "navy", font = ("Calibri", 20), width = 6, height = 2, command = leave)
            button3.place(x = 180, y = 175)
            
            canvas2.create_rectangle(25, 175, 135, 285, fill="lime", outline="black", width=3)
            canvas2.create_rectangle(50, 200, 110, 260, fill="lime", outline="black", width=3)
            canvas2.create_line(50, 200, 25, 175, fill="black", width=3)
            canvas2.create_line(110, 200, 135, 175, fill="black", width=3)
            canvas2.create_line(50, 260, 25, 285, fill="black", width=3)
            canvas2.create_line(110, 260, 135, 285, fill="black", width=3)
            
            
    else:
        lives -= 1
        label4.configure(text = "Wrong")
        label6.configure(text = "Lives:" + str(lives))


    if lives == 0:
        canvas1.destroy()
        label4.configure(text = "")
        canvas2 = Canvas(root, width = 300, height = 300, bg = "indigo")
        canvas2.place(x = 100, y = 100)
        label7 = Label(canvas2, text = "GAME OVER!", font = ("Calibri", 40), fg = "white", bg = "indigo")
        label7.place(x = 10, y = 25)
        label8 = Label(canvas2, text = str(treasure) + " treasure!", font = ("Calibri", 40), fg = "white", bg = "indigo")
        label8.place(x = 35, y = 100)
        button3 = Button(canvas2, text = "Exit", fg = "purple", bg = "navy", font = ("Calibri", 20), width = 6, height = 2, command = leave)
        button3.place(x = 110, y = 175)



button2 = Button(canvas1, text = "Dig!", fg = "purple", bg = "navy", font = ("Calibri", 15), width = 12, height = 3, command = dig)
button2.place(x = 10, y = 200)

root.mainloop()
