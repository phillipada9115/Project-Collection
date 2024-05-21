from tkinter import *
from PIL import ImageTk, Image
import random


root = Tk()
root.title("custom project 11")
root.geometry("600x600")
root.configure(bg = "cyan")

HitPoints = 100
enemy_hp = 130
preattack = 0
preattack_selection = 1
attack_damage = 0
shield = False
spell2 = False
round2plus = False
spell1_cd = -1
spell2_cd = -1

def attack():
    global label3, enemy_hp, enemy_turn
    enemy_hp -= 10

    enemy_turn()
    

def spell_1():
    global label3, enemy_hp, enemy_turn, HitPoints, shield, spell1_cd, statusshape
    enemy_hp -= 50
    if statusshape["bg"] == "red":
        shield = True
    elif statusshape["bg"] == "green" or statusshape["bg"] == "yellow":
        HitPoints += 15
    if HitPoints > 100:
        HitPoints = 100
    label1.configure(text = str(HitPoints)+"/100 HP")
    spell1_cd = 3
    button2.configure(text = str(spell1_cd),state = DISABLED)
    pass

def defend():
    global shield
    shield = True
    enemy_turn()

def spell_2():
    global spell2, spell2_cd
    spell2 = True
    spell2_cd = 3
    button4.configure(text = str(spell1_cd),state = DISABLED)
    enemy_turn()
    
def spell2_cast():
    global enemy_hp, HitPoints, spell2, attack_damage
    if spell2 == True:
        enemy_hp -= 2*attack_damage
        HitPoints *= 3
        HitPoints += 100
        HitPoints /= 4
        spell2 = False
    else:
        pass
    
    

def enemy1():
    global enemy_pic, enemy_hp, enemy_hp_string, enemyname
    enemy_pic = Image.open("Images/enemy 1.png")
    enemy_hp = 130
    enemy_hp_string = "/130"
    enemyname = "redface"
    
def enemy2():
    global enemy_pic, enemy_hp, enemy_hp_string, enemyname, round2plus
    enemy_pic = Image.open("Images/enemy 2.png")
    enemy_hp = 165
    enemy_hp_string = "/165"
    enemyname = "quadhex"
    button2.configure(text = "spell 1", state = NORMAL)
    button4.configure(text = "spell 2", state = NORMAL)
    round2plus = True
    
def enemy3():
    global enemy_pic, enemy_hp, enemy_hp_string, enemyname
    enemy_pic = Image.open("Images/enemy 3.png")
    enemy_hp = 150
    enemy_hp_string = "/150"
    enemyname = "svux"
    
def enemy4():
    global enemy_pic, enemy_hp, enemy_hp_string, enemyname
    enemy_pic = Image.open("Images/enemy 4.png")
    enemy_hp = 320
    enemy_hp_string = "/320"
    enemyname = "varone"

def enemy_turn():
    global statusshape, preattack, HitPoints, shield, preattack_selection, label3, label4, attack_damage
    attack_damage = 0
    check_enemy()
    if enemyname == "redface":
        if preattack == 1:
            attack_damage = 25
            preattack = 0
            statusshape.configure(bg = "green")        
        elif preattack == 0 :
            preattack_selection = random.randint(1, 3)
            if preattack_selection == 3:
                preattack = 1
                statusshape.configure(bg = "red")
                
    elif enemyname == "quadhex":
        if preattack == 1:
            attack_damage = 50
            preattack = 0
            statusshape.configure(bg = "green")
        elif preattack == 2 :
            attack_damage = 8
            preattack_selection = random.randint(1, 5)
            preattack = 0
            statusshape.configure(bg = "green")
        else:
            if enemy_hp < 80:
                preattack_selection = random.randint(1, 6)
            else:
                preattack_selection = random.randint(1, 4)
        if preattack_selection == 3:
            preattack = 1
            statusshape.configure(bg = "red")
        elif preattack_selection >= 4:
            preattack = 2
            statusshape.configure(bg = "yellow")
    
    elif enemyname == "svux":
        if preattack == 1:
            attack_damage = 30
            preattack = 0
            statusshape.configure(bg = "green")        
        elif preattack == 0 :
            pass
        preattack_selection = random.randint(1, 2)
        if preattack_selection == 2:
            preattack = 1
            statusshape.configure(bg = "red")
        elif preattack_selection == 1:
            preattack = 0
            statusshape.configure(bg = "green")
    
    elif enemyname == "varone":
        if preattack == 1:
            attack_damage = 75
            preattack = 0
            statusshape.configure(bg = "green")        
        elif preattack == 2:
            preattack = 1
            statusshape.configure(bg = "red")
        elif preattack == 0:
            preattack_selection = random.randint(1, 4)
            if preattack_selection == 4:
                preattack = 2
                statusshape.configure(bg = "yellow")
    
    if shield == True and attack_damage <= 25:
        attack_damage = 0
    elif shield == True and attack_damage > 25:
        attack_damage -= 25

    spell2_cast()
    shield = False
    HitPoints -= attack_damage
    int(HitPoints)
    check_enemy()
    label3.configure(text = str(enemy_hp)+enemy_hp_string, fg = "navy")
    label4.configure(text = str(HitPoints)+"/100 HP", fg = "navy")
    print(attack_damage)
    print(preattack)
            
    
def new_round():
    global enemy_pic, resized, newpic, label1, label2, label3, HitPoints, preattack
    resized = enemy_pic.resize((200, 200), Image.LANCZOS)
    newpic = ImageTk.PhotoImage(resized)
    label1 = Label(root, image = newpic)
    label1.place(x = 200, y = 25, width = 200, height = 200)
    label2.configure(text = enemyname)
    label3.configure(text = str(enemy_hp)+enemy_hp_string)
    statusshape.configure(bg = "green")
    preattack = 0
    HitPoints += 100
    HitPoints /= 2

    
def check_enemy():
    global spell1_cd, spell2_cd
    spell1_cd -= 1
    spell2_cd -= 1
    if round2plus == True:
        if spell1_cd >= 0:
            button2.configure(text = str(spell1_cd))
        if spell2_cd >= 0:
            button4.configure(text = str(spell2_cd))
    if spell1_cd == 0:
        button2.configure(text = "spell 1", state = NORMAL)
    if spell2_cd == 0:
        button4.configure(text = "spell 2", state = NORMAL)
    if enemy_hp <= 0:
        if enemyname == "redface":
            enemy2()
        elif enemyname == "quadhex":
            enemy3()
        elif enemyname == "svux":
            enemy4()
        new_round()
    
    if HitPoints <= 0:
        Canvas1 = Canvas(root, width = 600, height = 600, bg = "cyan")
        Canvas1.place(x = 0, y = 0)
        label5 = Label(Canvas1, text = "GAME OVER!", bg = "cyan", fg = "navy", font = "calibri 20")
        label5.place(x = 200, y = 200)

    


button1 = Button(root, text = "Attack", bg = "red", command = attack)
button1.place(x = 40, y = 300, width = 100, height = 100)

button2 = Button(root, text = "?", bg = "green", command = spell_1, state = DISABLED)
button2.place(x = 320, y = 300, width = 100, height = 100)

button3 = Button(root, text = "Defend", bg = "yellow", command = defend)
button3.place(x = 180, y = 300, width = 100, height = 100)

button4 = Button(root, text = "?", bg = "blue", command = spell_2, state = DISABLED)
button4.place(x = 460, y = 300, width = 100, height = 100)

#label1 = Label(root, image = newpic)
#label1.place(x = 200, y = 25, width = 200, height = 200)
label2 = Label(root, text = "", bg = "cyan", fg = "navy", font = "calibri 20")
label2.place(x = 400, y = 25)
label3 = Label(root, text = "", bg = "cyan", fg = "navy", font = "calibri 20")
label3.place(x = 400, y = 55)

label4 = Label(root, text = str(HitPoints)+"/100 HP", bg = "cyan", fg = "navy", font = "calibri 20")
label4.place(x = 25, y = 25)

label5 = Label(root, text = "Status:", bg = "cyan", fg = "navy", font = "calibri 20")
label5.place(x = 400, y = 85)

statusshape = Canvas(root, width = 25, height = 25, bg = "green", highlightthickness = 0)
statusshape.place(x = 485, y = 95)

enemy1()
new_round()



root.mainloop()