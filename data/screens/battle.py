import pygame
from data.handlers import fonthandler

class Soul():
    def __init__(self):
        self.image = pygame.image.load("data/images/ut-heart.png").convert_alpha()
        self.soulrect = self.image.get_rect()

        self.vel = 2

    def setPos(self, x, y):
        self.soulrect.x = x
        self.soulrect.y = y

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.soulrect.x -= self.vel
        elif keys[pygame.K_RIGHT]:
            self.soulrect.x += self.vel
            
        if keys[pygame.K_UP]:
            self.soulrect.y -= self.vel
        elif keys[pygame.K_DOWN]:
            self.soulrect.y += self.vel
        
    def update(self, display):
        display.blit(self.image, self.soulrect)

class Battle():
    def __init__(self):
        self.soul = Soul()
        
    def update(self, display):
        self.soul.move()
        self.soul.update(display)