from tkinter import *
from tkinter import ttk
from tkinter import colorchooser


root = Tk()
root.title("Custom Project 4")
root.geometry("1000x1000")
root.configure(background = "blue")


canvas = Canvas(root, width = 1400, height = 850, bg = "black")
canvas.place(x = 250, y = 100)


Label(root, text = "X placement", font = ("Courier", 10), bg = "blue").place(x=25, y = 25)
shapeX = Scale(root, from_=0, to=1400, orient = HORIZONTAL)
shapeX.place(x = 25, y = 50)
shapeXpos = int(shapeX.get())

Label(root, text = "Y placement", font = ("Courier", 10), bg = "blue").place(x=25, y = 100)
shapeY = Scale(root, from_=0, to=850, orient = HORIZONTAL)
shapeY.place(x = 25, y = 125)
#shapeYpos = 850 - int(shapeY.get())
shapeYpos = int(shapeY.get())

Label(root, text = "Size", font = ("Courier", 10), bg = "blue").place(x=25, y = 175)
shapeSize = Scale(root, from_=0, to=500, orient = HORIZONTAL)
shapeSize.place(x = 25, y = 200)
radius = int(shapeSize.get())

Label(root, text = "Border", font = ("Courier", 10), bg = "blue").place(x=25, y = 250)
shapeBorderW = Scale(root, from_=0, to=100, orient = HORIZONTAL)
shapeBorderW.place(x = 25, y = 275)

Label(root, text = "Shape", font = ("Courier", 10), bg = "blue").place(x=25, y = 325)
Shapestring = StringVar()
Shape = ttk.Combobox(root, width = 30, textvariable = Shapestring, state = "readonly")
Shape["values"] = ("Square", "Circle", "Triangle")
Shape.place(x = 25, y = 350)
Shape.current(0)

def choose_color():
    color_selection = colorchooser.askcolor(title = choose_color)
    color_code.configure(text = color_selection[1], fg = color_selection[1])
    
Label(root, text = "Color", font = ("Courier", 10), bg = "blue").place(x=25, y = 375)
colorbutton = Button(root, text = "Select color", command = choose_color)
colorbutton.place(x = 25, y = 400)
color_code = Label(root, text = "#fff", font = ("Courier", 10), fg = "#fff", bg = "blue")
color_code.place(x=25, y = 425)

def choose_color2():
    global color_code2
    color_selection2 = colorchooser.askcolor(title = choose_color)
    color_code2.configure(text = color_selection2[1], fg = color_selection2[1])

Label(root, text = "Boarder Color", font = ("Courier", 10), bg = "blue").place(x=25, y = 450)
colorbutton2 = Button(root, text = "Select color", command = choose_color2)
colorbutton2.place(x = 25, y = 475)
color_code2 = Label(root, text = "#000000", font = ("Courier", 10), fg = "#000000", bg = "blue")
color_code2.place(x=25, y = 500)

def draw():
    if Shape.get() == "Square":
        canvas.create_rectangle(int(shapeX.get())-int(shapeSize.get()), 850-int(shapeY.get())-int(shapeSize.get()),
                                int(shapeX.get())+int(shapeSize.get()), 850-int(shapeY.get())+int(shapeSize.get()),
                                fill = color_code["text"], outline =  color_code2["text"], width = int(shapeBorderW.get()))
        
    if Shape.get() == "Circle":
        canvas.create_oval(int(shapeX.get())-int(shapeSize.get()), 850-int(shapeY.get())-int(shapeSize.get()),
                            int(shapeX.get())+int(shapeSize.get()), 850-int(shapeY.get())+int(shapeSize.get()),
                            fill = color_code["text"], outline =  color_code2["text"], width = int(shapeBorderW.get()))
        
    if Shape.get() == "Triangle":
        canvas.create_polygon(int(shapeX.get())-int(shapeSize.get()), 850-int(shapeY.get())+int(shapeSize.get()),
                            int(shapeX.get()), 850-int(shapeY.get())-int(shapeSize.get()),
                            int(shapeX.get())+int(shapeSize.get()), 850-int(shapeY.get())+int(shapeSize.get()),
                            fill = color_code["text"], outline =  color_code2["text"], width = int(shapeBorderW.get()))


colorbutton2 = Button(root, text = "GO!", command = draw)
colorbutton2.place(x = 25, y = 550)

def erase():
    canvas.delete("all")

colorbutton2 = Button(root, text = "Erase.", command = erase)
colorbutton2.place(x = 25, y = 600)

root.mainloop()