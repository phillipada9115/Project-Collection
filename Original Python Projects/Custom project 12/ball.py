import pygame

class Ball:
    
    def __init__(self, surf, x, y, radius, xPrime, yPrime, color, borderwidth, pygame=pygame):
        self.surf = surf
        self.x = x
        self.y = y
        self.radius = radius
        self.xPrime = xPrime / 100
        self.yPrime = yPrime / 100
        self.color = color
        self.borderwidth = borderwidth
        
    def gravity(self, direction, strength):
        if direction == "up":
            if self.yPrime > 0 and self.yPrime < strength:
                self.yPrime = -self.yPrime 
            elif  self.yPrime > 0.75:
                self.yPrime = self.yPrime - strength
        elif direction == "down":
            self.yPrime = self.yPrime + strength / 1000
        elif direction == "left":
            self.xPrime = self.xPrime - strength / 1000
        elif direction == "right":
            self.xPrime = self.xPrime + strength / 1000
        elif direction == "slow":
            self.xPrime = -(strength**2) / 100
            self.yPrime = -strength**2 / 100
        

        
        
        
    #edit next
    def move(self):
        if (self.x > 1500 - self.radius or self.x < self.radius):
            self.xPrime = -self.xPrime
        if (self.y > 900 - self.radius or self.y < self.radius):
            self.yPrime = -self.yPrime
        
        self.x = self.x + self.xPrime
        self.y = self.y + self.yPrime
        self.image =  pygame.draw.circle(self.surf, self.color, (self.x, self.y), self.radius, self.borderwidth)
        
        
        
        pass
