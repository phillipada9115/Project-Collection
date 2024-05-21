import pygame
from ball import *


pygame.init()

surf = pygame.display.set_mode((1500, 900), pygame.SRCALPHA, 32)
pygame.display.set_caption("Custom project 12")
surf.fill("navy")


def balls():
    global bubble, vollyball, basketball, golfball1, golfball2, golfball3, \
    tennisball, black_hole, frisbee, marble
    bubble = Ball(surf, 400, 400, 300, 1, 1, "cyan", 15)
    vollyball = Ball(surf, 200, 200, 25, 2, 3, "White", 10)
    basketball = Ball(surf, 200, 200, 100, 3, 5, "orange", 8)
    golfball1 = Ball(surf, 200, 200, 8, 10, 9, "white", 8)
    golfball2 = Ball(surf, 200, 200, 8, 11, 9, "green", 8)
    golfball3 = Ball(surf, 200, 200, 8, 12, 9, "red", 8)
    tennisball = Ball(surf, 200, 200, 30, 15, -10, "lime", 10)
    black_hole = Ball(surf, 300, 300, 100, 0, 0, "black", 100)
    frisbee = Ball(surf, 300, 300, 200, 5, -2, "purple", 75)
    marble = Ball(surf, 300, 300, 50, 0.02, 0.05, "pink", 3)


clock = pygame.time.Clock()
gravityD = False
gravityS = False
gravityW = False
gravityA = False

balls()
font = pygame.font.Font(None, 75)
text = font.render( "Custom Project 12", True, "white")
textrect = text.get_rect()
textrect.center = (250, 50)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if gravityD == True:
                    gravityD = False
                else:
                    gravityD = True
            if event.key == pygame.K_w:
                bubble.gravity("up", 0.5)
                vollyball.gravity("up", 0.8)
                basketball.gravity("up", 1.5)
                golfball1.gravity("up", 1)
                golfball2.gravity("up", 1)
                golfball3.gravity("up", 1)
                tennisball.gravity("up", 0.5)
                black_hole.gravity("up", 0.5)
                frisbee.gravity("up", 2)
                marble.gravity("up", 0.5)
            if event.key == pygame.K_a:
                for i in range(100):
                    bubble.gravity("left", 3)
                    vollyball.gravity("left", 3)
                    basketball.gravity("left", 3)
                    golfball1.gravity("left", 3)
                    golfball2.gravity("left", 3)
                    golfball3.gravity("left", 3)
                    tennisball.gravity("left", 3)
                    black_hole.gravity("left", 3)
                    frisbee.gravity("left", 3)
                    marble.gravity("left", 0.3)
            if event.key == pygame.K_s:
                if gravityS == True:
                    gravityS = False
                else:
                    gravityS = True
            if event.key == pygame.K_q:
                balls()
            
            elif event.key == pygame.K_e:
                bubble.gravity("slow", 0.5)
                vollyball.gravity("slow", 0.8)
                basketball.gravity("slow", 1.5)
                golfball1.gravity("slow", 1)
                golfball2.gravity("slow", 1)
                golfball3.gravity("slow", 1)
                tennisball.gravity("slow", 0.5)
                black_hole.gravity("slow", 0)
                frisbee.gravity("slow", 2)
                marble.gravity("slow", 0.2)
                
        
        if event.type == pygame.QUIT:                
            running = False
    
    surf.fill("navy")
    surf.blit(text, textrect)
    
    bubble.move()
    vollyball.move()
    basketball.move()
    golfball1.move()
    golfball2.move()
    golfball3.move()
    tennisball.move()
    black_hole.move()
    frisbee.move()
    for i in range(10):
        marble.move()
    
    if gravityS == True:
        bubble.gravity("down", 0.1)
        vollyball.gravity("down", 0.5)
        basketball.gravity("down", 0.6)
        golfball1.gravity("down", 0.7)
        golfball2.gravity("down", 0.8)
        golfball3.gravity("down", 0.9)
        tennisball.gravity("down", 1)
        black_hole.gravity("down", 1.2)
        frisbee.gravity("down", 2)
        marble.gravity("down", 0.2)
    
    if gravityD == True:
        bubble.gravity("right", 0.1)
        vollyball.gravity("right", 0.5)
        basketball.gravity("right", 0.6)
        golfball1.gravity("right", 0.7)
        golfball2.gravity("right", 0.8)
        golfball3.gravity("right", 0.9)
        tennisball.gravity("right", 1)
        black_hole.gravity("right", 1.2)
        frisbee.gravity("right", 2)
        marble.gravity("right", 0.2)

    pygame.display.update()
                    
    
     
     

