from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

root = Tk()
root.title("Custom Project 8")
root.geometry("600x500")
root.configure(bg = "blue")

label1 = Label(root, text="Scatter graph maker", bg="blue", fg="white", font = "Calibri 30")
label1.place(x = 10, y = 10)

canvas1 = Canvas(root, width = 500, height = 400, bg = "indigo", highlightthickness = 0)
canvas1.place(x = 50, y = 75)

label2 = Label(canvas1, text="Alpha", bg="indigo", fg="white", font = "Calibri 15")
label2.place(x = 0, y = 0)
alpha = Scale(canvas1, from_=1, to=10, orient = HORIZONTAL, length = 200)
alpha.place(x = 5, y = 25)

label3 = Label(canvas1, text="Amount", bg="indigo", fg="white", font = "Calibri 15")
label3.place(x = 0, y = 75)
amount = Scale(canvas1, from_=10, to=2000, orient = HORIZONTAL, length = 200)
amount.place(x = 5, y = 100)

label4 = Label(canvas1, text="Size", bg="indigo", fg="white", font = "Calibri 15")
label4.place(x = 0, y = 150)
maxsize = Scale(canvas1, from_=10, to=2000, orient = HORIZONTAL, length = 200)
maxsize.place(x = 5, y = 175)

label5 =Label(canvas1, text = "Formation", bg = "indigo", fg = "white", font = "Calibri 15")
label5.place(x= 0, y = 225)
Formstring = StringVar()
Form = ttk.Combobox(canvas1, width = 30, textvariable = Formstring, state = "readonly")
Form["values"] = ("Fixed", "Cluster", "Path", "Trend")
Form.place(x = 5, y = 250)
Form.current(0)

label6 =Label(canvas1, text = "Color Pack", bg = "indigo", fg = "white", font = "Calibri 15")
label6.place(x= 0, y = 275)
Colorpackstring = StringVar()
Colorpack = ttk.Combobox(canvas1, width = 30, textvariable = Colorpackstring, state = "readonly")
Colorpack["values"] = ("viridis", "plasma", "inferno", "magma", "cividis",
    "spring", "summer", "autumn", "winter", "cool", "Wista", "hot", "Spectral", "seismic", "twilight", "ocean")
Colorpack.place(x = 5, y = 300)
Colorpack.current(0)

label7 =Label(canvas1, text = "Size Disparities", bg = "indigo", fg = "white", font = "Calibri 15")
label7.place(x= 0, y = 325)
Sizestring = StringVar()
Size = ttk.Combobox(canvas1, width = 30, textvariable = Sizestring, state = "readonly")
Size["values"] = ("Equal", "inc by XY", "Random", "Color influenced")
Size.place(x = 5, y = 350)
Size.current(0)

label8 =Label(canvas1, text = "Shape", bg = "indigo", fg = "white", font = "Calibri 15")
label8.place(x= 250, y = 225)
Shapestring = StringVar()
Shape = ttk.Combobox(canvas1, width = 30, textvariable = Shapestring, state = "readonly")
Shape["values"] = ("o", "s", "X", "H", "D", "*")
Shape.place(x = 255, y = 250)
Shape.current(0)

label9 =Label(canvas1, text = "Color Disparities", bg = "indigo", fg = "white", font = "Calibri 15")
label9.place(x= 250, y = 275)
Colorstring = StringVar()
Color = ttk.Combobox(canvas1, width = 30, textvariable = Colorstring, state = "readonly")
Color["values"] = ("XY influenced", "vomnises", "random","pareto")
Color.place(x = 255, y = 300)
Color.current(0)

label10 =Label(canvas1, text = "Style", bg = "indigo", fg = "white", font = "Calibri 15")
label10.place(x= 250, y = 325)
Stylestring = StringVar()
Style = ttk.Combobox(canvas1, width = 30, textvariable = Stylestring, state = "readonly")
Style["values"] = ("default", "classic", "bmh", "ggplot", "fast","fivethirtyeight", "dark_background", "seaborn-v0_8")
Style.place(x = 255, y = 350)
Style.current(0)

def generate():
    global maxsize, amount, Form, Colors, Size, Shape
    plt.style.use(Stylestring.get())
    
    count = int(amount.get())
    
    if Form.get() == "Fixed":
        count2 = round(np.sqrt(count))
        count = count2**2
        dots = np.linspace(0, 1, count2)
        X, Y = np.meshgrid(dots, dots)
        x, y = X.ravel(), Y.ravel()
    elif Form.get() == "Cluster":
        x = np.random.rand(count)
        y = np.random.rand(count)
    elif Form.get() == "Path":
        x = np.random.rand(count)
        y = x**1.1
    elif Form.get() == "Trend":
        x = np.random.rand(count)
        y = x*np.random.randn(count)
    
    
    if Color.get() == "XY influenced":
        color = x+y
    elif Color.get() == "vomnises":
        color = np.random.vonmises(0, np.pi, count)
    elif Color.get() == "random":
        color = np.random.rand(count)
    elif Color.get() == "pareto":
        color = np.random.pareto(100, count)
    
    colormap = str(Colorpack.get())
    Alpha = int(alpha.get())/10
    
    
    size2 = int(maxsize.get())
    if Size.get() == "Equal":   
        size = size2
    elif Size.get() == "inc by XY":
        size = size2*(0.1+x+y)
    elif Size.get() == "Random":
        size = np.random.randint(0, size2, count)
    elif Size.get() == "Color influenced":
        size = size2*(0.5+color)
        
    marker = str(Shape.get())

    
    plt.scatter(x, y, c = color, cmap = colormap, s = size, marker = marker, alpha = Alpha)
    plt.title("Custom Project 8")
    plt.show()


Button1 = Button(canvas1, text = "GO!", width = 7, height = 2, bg = "blue", fg = "indigo", font= "Calibri 45", command = generate)
Button1.place(x = 250, y= 25)




root.mainloop()