canvas = Canvas(root, width=400, height=125, bg="purple")
canvas.place(x = 100, y = 50)

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