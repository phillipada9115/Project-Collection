import pygame
import random
import numpy as np
import block_generatior as BlockGen

 


     
pygame.init()

clock = pygame.time.Clock()


surf = pygame.display.set_mode((1500, 1000))
pic1 = pygame.image.load("king phi 1.2.png")
pic1 = pygame.transform.scale(pic1, (75,100))
dx = 0
y = 0
x2 = 200
y2 = 200
ticks = 0
total_ticks = 0
score = 0
level = 1
bgcolor = "white"


font = pygame.font.Font(None, 50)  
font2 = pygame.font.Font(None, 100)  


color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
dx_list = [0, 0, 0, -1, 1]
dy_list = [1, 2, 3]
block_list = []
game_over = False


def make_block():
    global x, y, dx, dy, width, height, color, boarder_width, block, block_list
    x = random.randint(-50, 1450)
    y = 0
    dx = random.choice(dx_list)
    dy = random.choice(dy_list)
    width = random.randint(15, 300)
    height = random.randint(15, 300)
    boarder_width = random.randint(5, 75)
    color = random.choice(color_list)
    block = BlockGen.Block(surf, x, y, dx, dy, color, width, height, boarder_width)
    block_list.append(block)
    for block in block_list:
            block.draw()
    


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                
            running = False
    keys = pygame.key.get_pressed()
    surf.fill(bgcolor)
    
    
    ticks += 1
    total_ticks += 1
    if ticks == 60 and game_over == False:
        score += 1
        ticks = 0
        make_block()
        block = BlockGen.Block(surf, x, y, dx, dy, color, width, height, boarder_width)
        block_list.append(block)
    
    for block in block_list:
        block.draw()
    
        if score > 0:
            block.detect_collision(hitbox)
            if block.detect_collision(hitbox) == True:
                game_over = True
    
    
    
    if keys[pygame.K_LEFT]:
        x2 -= 5
    if keys[pygame.K_RIGHT]:
        x2 += 5
    if keys[pygame.K_UP]:
        y2 -= 5
    if keys[pygame.K_DOWN]:
        y2 += 5
    
    if x2 < 0:
        x2 = 0
    if x2 > 1425:
        x2 = 1425
    if y2 < 0:
        y2 = 0
    if y2 > 900:
        y2 = 900
    
    text = font.render(str(score) + " Points", True, "black") 
    text_rect = text.get_rect()
    text_rect.center = (100, 25)
    surf.blit(text, text_rect)
    hitbox = pygame.Rect(x2, y2, 75, 100)
    king_phi = surf.blit(pic1, (x2,y2))
    
    
    
    if score % 5 == 0 and ticks == 0:
        if score == 5:
            new_color_list = ["pink", "lavender", "lime", "white", "black"]
            new_dx_list = [-2, -0.5, 0.5, 2]
            new_dy_list = [0.5, 1.5, 3]
            level = 2
            bgcolor = "teal"
        elif score == 15:
            new_color_list = [ "teal", "navy", "gray","magenta", "gold"]
            new_dx_list = [-3, 3]
            new_dy_list =[0.25, 4, 5]
            level = 3
            bgcolor = "cyan"
        else:
            new_color_list =[]
            new_dx_list = []
            new_dy_list = []

        for i in range(len(new_color_list)):
            color_list.append(new_color_list[i- 1])
        for i in range(len(new_dx_list)):
            dx_list.append(new_dx_list[i- 1])
        for i in range(len(new_dy_list)):
            dy_list.append(new_dy_list[i- 1])
    
    
    if level >= 2 and total_ticks % 40 == 0:
        make_block()
    
    if level >= 3 and total_ticks % 33 == 0:
        make_block()
        
    
    
    if game_over == True:
        game_over_text = font2.render("GAME OVER!", True, "black")
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (surf.get_width() / 2, surf.get_height() / 2 + 50)
        surf.blit(game_over_text, game_over_rect)
        
        game_over_text2 = font2.render("U got " + str(score) + " Points!", True, "black")
        game_over_rect2 = game_over_text2.get_rect()
        game_over_rect2.center = (surf.get_width() / 2, surf.get_height() / 2 - 50)
        surf.blit(game_over_text2, game_over_rect2)
        if ticks == 180:
            pygame.quit()
    
    pygame.display.update()
    clock.tick(60)
     
     

