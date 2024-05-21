from tkinter import *
from tkinter import ttk
from turtle import *
import random


root = Tk()
root.title("Custom Project 6")
root.geometry("400x400")


def start():
    global button1, treasure, command2_1, command3_1,command4_6, command6_1, shape1selection, shape2selection, shape3selection
    root.configure(bg = "cyan")
    button1 = Button(root, width = 15, height = 8, text = "Click me", command = command1, bg = "white")
    button1.place(x = 100, y = 100)
    treasure = 0
    command2_1 = True
    command3_1 = True
    command4_6 = True
    command6_1 = True
    shape1selection = 0
    shape2selection = 0
    shape3selection = 0



  
    
def command1():
    global treasure, command4_6
    x = random.randint(0, 1600)
    y = random.randint(0, 800)
    button1.pack_forget()
    button1.place(x = x, y = y)
    if x >= 600 and x <= 1200 and y >= 200 and y <= 800:
        button1.config(text ="try pressing space", bg = "green")
    elif shape1selection == 0 and shape2selection == 2 and shape3selection == 2 and command4_6 == True:
        button1.config(text = "u got treasure", bg = "gold")
        treasure += 1
        command4_6 = False
    else:
        button1.config(text = "Click me", bg = "white")
      
        
def command2(event):
    global treasure, command2_1, path, canvas
    if command2_1 == True:
        canvas = Canvas(root, width = 500, height = 500)
        canvas.place(x = 1150, y = 450)
        command2_1 = False
        pathstring = StringVar()
        path = ttk.Combobox(canvas, width = 30, textvariable = pathstring, state = "readonly")
        path["values"] = ("I", "II", "III","IV")
        path.place(x = 25, y = 25)
        path.current(0)
        button2 = Button(canvas, text = "Let's go", width = 10, height = 5, command = command3)
        button2.place(x = 25, y = 50)


        if button1["text"] == "Click me":
            treasure += 1
    else:
        command1()
    
def command3():
    global treasure, canvas2, shape1, shape2, shape3, label1, label2, label3, command3_1
    if path.get() == "I":
        root.destroy()
    elif path.get() == "II":
        command1()
    elif path.get() == "III":
        canvas2 = Canvas(root, width = 200, height = 70, bg = "black")
        canvas2.place(x = 1000, y = 175)
        shape1 = canvas2.create_oval( 10, 10, 60, 60, fill = "red")
        shape2 = canvas2.create_oval( 70, 10, 120, 60, fill = "yellow")
        shape3 = canvas2.create_oval( 130, 10, 180, 60, fill = "blue")
        
        button3 = Button(canvas, text = "1", width = 4, height = 2, bg = "red", command = command4_1)
        button3.place(x = 250, y = 25)
        button4 = Button(canvas, text = "2", width = 4, height = 2, bg = "yellow", command = command4_2)
        button4.place(x = 300, y = 25)
        button5 = Button(canvas, text = "3", width = 4, height = 2, bg = "blue", command = command4_3)
        button5.place(x = 350, y = 25)
        button6 = Button(canvas, text = "GO!", width = 4, height = 2, bg = "green", command = command4_4)
        button6.place(x = 400, y = 25)
    elif path.get() == "IV":
        label1 = Label(root, text = "circle, square, square", font = ("Courier", 20), bg = "cyan")
        label1.place(x = 1000, y = 25)
        label2 = Label(root, text = "press jumping button after", font = ("Courier", 20), bg = "cyan")
        label2.place(x = 1000, y = 75)
        label3 = Label(root, text = "answer is submitted.", font = ("Courier", 20), bg = "cyan")
        label3.place(x = 1000, y = 125)
    else:
        if command3_1 == True:
            treasure += 1
            command3_1 = False
        else:
            pass
        
        
        
def command4_1():
    global shape1selection, shape1
    canvas2.delete(shape1)
    if shape1selection == 2:
        shape1selection = 0
    else:
        shape1selection += 1
    if shape1selection == 0:
        shape1 = canvas2.create_oval( 10, 10, 60, 60, fill = "red")
    elif shape1selection == 1:
        shape1 = canvas2.create_polygon( 10, 60, 35, 10, 60, 60, fill = "red")
    elif shape1selection == 2:
        shape1 = canvas2.create_rectangle( 10, 10, 60, 60, fill = "red")
        

        
def command4_2():
    global shape2selection, shape2
    canvas2.delete(shape2)
    if shape2selection == 2:
        shape2selection = 0
    else:
        shape2selection += 1
    if shape2selection == 0:
        shape2 = canvas2.create_oval( 70, 10, 120, 60, fill = "yellow")
    elif shape2selection == 1:
        shape2 = canvas2.create_polygon( 70, 60, 95, 10, 120, 60, fill = "yellow")
    elif shape2selection == 2:
        shape2 = canvas2.create_rectangle( 70, 10, 120, 60, fill = "yellow")
def command4_3():
    global shape3selection, shape3
    canvas2.delete(shape3)
    if shape3selection == 2:
        shape3selection = 0
    else:
        shape3selection += 1
    if shape3selection == 0:
        shape3 = canvas2.create_oval( 130, 10, 180, 60, fill = "blue")
    elif shape3selection == 1:
        shape3 = canvas2.create_polygon( 130, 60, 155, 10, 180, 60, fill = "blue")
    elif shape3selection == 2:
        shape3 = canvas2.create_rectangle( 130, 10, 180, 60, fill = "blue")
        
def command5(event):
    global canvas3, path2, label6, label5
    canvas3 = Canvas(root, width = 500, height = 500, bg = "indigo")
    canvas3.place(x = 100, y = 400)
    
    label5 = Label(canvas3, text = "Color of this box?", font = ("Courier", 20), fg = "white", bg = "indigo")
    label5.place(x = 25, y = 5)
    
    pathstring2 = StringVar()
    path2 = ttk.Combobox(canvas3, width = 30, textvariable = pathstring2, state = "readonly")
    path2["values"] = ("red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "white", "black", "treasure")
    path2.place(x = 25, y = 75)
    path2.current(0)
    
    button7 = Button(canvas3, text = "Submit", width = 10, height = 5, command = command6)
    button7.place(x = 25, y = 125)
    
    label6 = Label(canvas3, text = "", font = ("Courier", 20), fg = "white", bg = "indigo")
    label6.place(x = 25, y = 225)
    



        
def command4_4():
    global label4
    if shape1selection == 0 and shape2selection == 2 and shape3selection == 2:
        root.bind("<q>", command5)
        label4 = Label(root, text = "press q", font = ("Courier", 20), bg = "cyan")
        label4.place(x = 25, y = 25)
        
        
def command6():
    global treasure, path2, label6, command6_1
    if path2.get() == "treasure" and command6_1 == True:
        label6.config(text = "plus one treasure!")
        treasure += 1
        command6_1 = False
    elif path2.get() == "indigo":
        canvas4 = Canvas(root, width = 500, height = 500, bg = "lime")
        canvas4.place(x = 500, y = 200)
        
        button8 = Button(canvas4, text = "goodbye", width = 20, height = 10, bg = "green", command = command7)
        button8.place(x = 200, y = 200)
        
        label7 = Label(canvas4, text = "U WIN!", font = ("Courier", 20), fg = "white", bg = "lime")
        label7.place(x = 100, y = 10)
        
        label8 = Label(canvas4, text = "U got " + str(treasure) + " treasure!", font = ("Courier", 20), fg = "white", bg = "lime")
        label8.place(x = 100, y = 50)
        
        label6.config(text = "U WIN!")
        label5.config(text = "U WIN!")
        label5.config(text = "U WIN!")
        label4.config(text = "U WIN!")
        label3.config(text = "U WIN!")
        label2.config(text = "U WIN!")
        label1.config(text = "U WIN!")
        
        
        
        
        
    elif path2.get() == "violet" or path2 == "blue":
        label6.config(text = "close lol")
    else:
        label6.config(text = "wrong")
        
def command7():
    root.destroy()
            





root.bind("<space>", command2)
    
    

start()
root.mainloop()