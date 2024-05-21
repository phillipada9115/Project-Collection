from tkinter import *
import random



root = Tk()
root.title("Custom Project 5")
root.geometry("500x500")
root.configure(bg = "indigo")

canvas = Canvas(root, width =1770, height = 900, bg = "lime")
canvas.place(x = 0, y = 100)

color_list = ["brown", "red", "orange", "gold", "yellow", "green", "cyan", "teal",
              "blue", "indigo", "purple", "pink", "white", "gray", "black"]

message = ["King Phi is the best.", "King Phi made this.", "Did you train today?", "Single jacked kings are a paradox.",
           "Don't be a nerd, ok?!", "I deserve some $.", "I am always a berserker.", "King phi worked hard making this.",
           "King phi's summons'll replace u.", "I like teasing ppl.","Bragging increases my intellegence quotient."]

label = Label(root, text = "King Phi's project!", bg = "indigo", fg = "navy", font = ("calibri", 30))
label.place(x = 50, y = 25)

def setup():
    global x, y, z, fill4, outline4, fill5, outline5, player_image, enemy_image, mychar, shape2, shape3, shape4, shape5, enemy_4
    x = 625
    y = 350
    z = 1
    fill4 = "yellow"
    outline4 = "pink"
    fill5 = 3
    outline5 = 2
    player_image=PhotoImage(file="king phi 1.0.png")
    enemy_image=PhotoImage(file="enemy 4.png")
    mychar= canvas.create_image(200,360,image=player_image)
    #mychar = canvas.create_rectangle(625, 350, 655, 380, fill = "red")
    shape2 = canvas.create_oval(1000, 700, 1100, 800, fill = "blue", outline = "cyan", width = 25)
    shape3 = canvas.create_rectangle(1200, 200, 1400, 400, fill = "red", outline = "cyan", width = 1)
    shape4 = canvas.create_polygon(100, 100, 150, 200, 200, 100, fill = fill4, outline = outline4, width = 35)
    shape5 =canvas.create_rectangle(200, 600, 350, 750, fill = color_list[fill5], outline = color_list[outline5], width = 50)
    enemy_4 = canvas.create_image(700, 500, image = enemy_image)

    
setup()

def left(event):
    if canvas.coords(mychar)[0]>0:
        canvas.move(mychar,-10,0)
def right(event):
    if canvas.coords(mychar)[0]<1675:
        canvas.move(mychar,10,0)
def up(event):
    if canvas.coords(mychar)[1]>0:
        canvas.move(mychar,0,-10)
def down(event):
    if canvas.coords(mychar)[1]<865:
        canvas.move(mychar,0,10)
        

def enemyleft(event):
    if canvas.coords(enemy_4)[0]>0:
        canvas.move(enemy_4,-10,0)
def enemyright(event):
    if canvas.coords(enemy_4)[0]<1675:
        canvas.move(enemy_4,10,0)
def enemyup(event):
    if canvas.coords(enemy_4)[1]>0:
        canvas.move(enemy_4,0,-10)
def enemydown(event):
    if canvas.coords(enemy_4)[1]<865:
        canvas.move(enemy_4,0,10)


print(canvas.coords(shape2)[0])
print(canvas.coords(shape2)[1])
        

def teleport(event):
    global shape2
    x = random.randint(100, 1575)
    y = random.randint(100, 765)
    canvas.delete(shape2)
    shape2 = canvas.create_oval(x, y, x+100, y+100, fill = "blue", outline = "cyan", width = 25)
    
def thicken(event):
    global z
    if z < 75:
        global shape3
        z += 1
        canvas.delete(shape3)
        shape3 = canvas.create_rectangle(1200, 200, 1400, 400, fill = "red", outline = "cyan", width = z)
        root.after(50, thicken)
        
def trim(event):
    global z
    global shape3
    if z > 15:
        z -= 15
        canvas.delete(shape3)
        shape3 = canvas.create_rectangle(1200, 200, 1400, 400, fill = "red", outline = "pink", width = z)
        
    elif z <= 15:
        z = 1
        canvas.delete(shape3)
        shape3 = canvas.create_rectangle(1200, 200, 1400, 400, fill = "red", outline = "pink", width = z)
        
        

        
def fillhue(event):
    global shape4, shape5, fill4, fill5
    fill4 = random.choice(color_list)
    fill5 += 1
    if fill5 > 14:
        fill5 = 0
    canvas.delete(shape4)
    canvas.delete(shape5)
    shape4 = canvas.create_polygon(100, 100, 150, 200, 200, 100, fill = fill4, outline = outline4, width = 35)
    shape5 = canvas.create_rectangle(200, 600, 350, 750, fill = color_list[fill5], outline = color_list[outline5], width = 50)

    
def outlinehue(event):
    global shape4, shape5, outline4, outline5
    outline4 = random.choice(color_list)
    outline5 += 1
    if outline5 > 14:
        outline5 = 0
    canvas.delete(shape4)
    canvas.delete(shape5)
    shape4 = canvas.create_polygon(100, 100, 150, 200, 200, 100, fill = fill4, outline = outline4, width = 35)
    shape5 = canvas.create_rectangle(200, 600, 350, 750, fill = color_list[fill5], outline = color_list[outline5], width = 50)
    
def reset():
    global label
    canvas.delete("all")
    setup()
    button.destroy()
    label.configure(text = "King Phi's project!")
    
    
def reset_button(event):
    global button
    button = Button(root, width=10, height=3, bg = "blue", text = "Reset", fg = "purple", command = reset)
    button.place(x = 1500, y = 25)
    
def rain(event):
    x = random.randint(25, 1650)
    y = random.randint(25, 775)
    canvas.create_oval(x, y, x+25, y+25, fill = "blue", outline = "teal", width = 5)
        
def npc(event):
    global label
    text = random.choice(message)
    label.configure(text = text)
    


root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.bind("<a>",enemyleft)
root.bind("<d>",enemyright)
root.bind("<w>",enemyup)
root.bind("<s>",enemydown)

root.bind("<q>", teleport)
root.bind("<z>", thicken)
root.bind("<x>", trim)
root.bind("<c>", fillhue)
root.bind("<v>", outlinehue)
root.bind("<e>", reset_button)
root.bind("<f>", rain)
root.bind("<r>", npc)

#root.bind("<space>",make_candy)




root.mainloop()
