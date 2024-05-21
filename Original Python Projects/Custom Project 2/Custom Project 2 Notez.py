If enviornment == "1":
    t.color(color3)    
    A1_1()
    size = int(size)/2
    t.color(color2)
    t.begin_fill()
    A1_1()
    t.end_fill()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    for k in range(5):
        size = 25
        t.color(color4)
        t.begin_fill()
        A1_1()
        t.end_fill()
        t.penup()
        t.left(60)
        t.forward(40)
        t.pendown()
        A1_1()
        t.right(120)
        t.penup()
        t.forward(40)
        t.pendown()
        t.left(60)

elif enviornment == "2":
    for k in range(3):
        t.color(color3)    
        A1_1()
        t.right(120)
    
    
    size = int(size)/2
    t.color(color2)
    
    for l in range(6):
        t.begin_fill()
        A1_1()
        t.end_fill()
        t.penup()
        t.left(60)
        t.forward(50)
        t.pendown()
        size += 10
elif enviornment == "3":
    t.goto(300,300)
    for k in range(6):
        for l in range(3):
            t.color(color1)    
            A1_1()
            t.right(120)
            size += 5
        t.right(120)
        t.forward(100)
    for m in range(3):
        size = 40
        for n in range(10):
            t.begin_fill()
            A1_1()
            t.end_fill()
            t.penup()
            t.left(36)
            t.forward(50)
            t.pendown()
            pensize = pensize + 1
            t.pensize(pensize)
            size += 10
        t.right(120)
        t.forward(100)