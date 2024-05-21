from tkinter import *


root = Tk()
root.geometry("600x600")
root.title("Custom Project 7")
root.config(bg="black")

Label(root, text="King Phi's turtle art collection", bg="black", fg="white", font=("Calibri", 13)).place(x = 100, y = 10)

canvas = Canvas(root, width=400, height=125, bg="purple")
canvas.place(x = 100, y = 150)

def opendrawing1_1():
    import Drawing1_1

    
def opendrawing1_2():
    import Drawing1_2
    
def opendrawing1_3():
    import Drawing1_3
    

button1_1 = Button(canvas, text="Press Me", bg="red", fg="purple",
                   width = 10, height = 5, command = opendrawing1_1)
button1_1.place(x = 25, y = 20)

button1_2 = Button(canvas, text="Press Me", bg="yellow", fg="purple",
                   width = 10, height = 5, command = opendrawing1_2)
button1_2.place(x = 162.5, y = 20)

button1_3 = Button(canvas, text="Press Me", bg="blue", fg="purple",
                   width = 10, height = 5, command = opendrawing1_3)
button1_3.place(x = 300, y = 20)


canvas2 = Canvas(root, width=400, height=125, bg="navy")
canvas2.place(x = 100, y = 300)

def opendrawing2_1():
    import Drawing2_1
    
def opendrawing2_2():
    import Drawing2_2
    
    
def opendrawing2_3():
    import Drawing2_3
    

button2_1 = Button(canvas2, text="Press Me", bg="red", fg="navy",
                   width = 10, height = 5, command = opendrawing2_1)
button2_1.place(x = 25, y = 20)

button2_2 = Button(canvas2, text="Press Me", bg="yellow", fg="navy",
                   width = 10, height = 5, command = opendrawing2_2)
button2_2.place(x = 162.5, y = 20)

button2_3 = Button(canvas2, text="Press Me", bg="blue", fg="navy",
                   width = 10, height = 5, command = opendrawing2_3)
button2_3.place(x = 300, y = 20)



canvas3 = Canvas(root, width=400, height=125, bg="cyan")
canvas3.place(x = 100, y = 450)

def opendrawing3_1():
    import Drawing3_1
    
def opendrawing3_2():
    import Drawing3_2
    
def opendrawing3_3():
    import Drawing3_3
    

button3_1 = Button(canvas3, text="Press Me", bg="red", fg="cyan",
                   width = 10, height = 5, command = opendrawing3_1)
button3_1.place(x = 25, y = 20)

button3_2 = Button(canvas3, text="Press Me", bg="yellow", fg="cyan",
                   width = 10, height = 5, command = opendrawing3_2)
button3_2.place(x = 162.5, y = 20)

button3_3 = Button(canvas3, text="Press Me", bg="blue", fg="cyan",
                   width = 10, height = 5, command = opendrawing3_3)
button3_3.place(x = 300, y = 20)

#def refresh():
#    root.destroy()


#button4 = Button(root, text="Exit", bg="white", fg="black",
#                   width = 10, height = 5, command = refresh)
#button4.place(x = 500, y = 25)

root.mainloop()