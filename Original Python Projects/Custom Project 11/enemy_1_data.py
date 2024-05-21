from tkinter import *
from PIL import ImageTk, Image
import main

def enemy1():
    global enemy_pic, enemy_hp, enemy_hp_string, enemyname
    enemy_pic = Image.open("Images/enemy 1.png")
    enemy_hp = 30
    enemy_hp_string = "/30"
    enemyname = "redface"
    
def new_round():
    global enemy_pic, resized, newpic, label1, label2, label3
    resized = enemy_pic.resize((200, 200), Image.LANCZOS)
    newpic = ImageTk.PhotoImage(resized)
    label1 = Label(root, image = newpic)
    label1.place(x = 200, y = 25, width = 200, height = 200)
    label2 = Label(root, text = enemyname, bg = "cyan", fg = "navy", font = "calibri 20")
    label2.place(x = 400, y = 50)
    label3 = Label(root, text = str(enemy_hp)+enemy_hp_string, bg = "cyan", fg = "navy", font = "calibri 20")
    label3.place(x = 400, y = 100)
