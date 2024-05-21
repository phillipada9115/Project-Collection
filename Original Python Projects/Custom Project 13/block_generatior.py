import pygame
import random

class Block:
    def __init__(self, surf, x, y, dx, dy, color, width, height, boarder_width, pygame=pygame):
        self.x = x
        self.y = y
        self.dy = dy
        self.dx = dx
        self.color = color
        self.width = width
        self.height = height
        self.boarder_width = boarder_width
        self.surf = surf
        
    def draw(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.block = pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.width, self.height), self.boarder_width)
        
        
    def detect_collision(self, king_phi):
        if self.block.colliderect(king_phi):
            return True
        


class LevelUp:
    def init(self, level, pygame=pygame):
        self.level = level
        if self.level == 2:
            pass