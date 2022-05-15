import pygame

pygame.init()

class Font():
    def __init__(self, path, size, text=None):
        self.font = path
        self.text = text
        self.size = size
        
        self.textfont = pygame.font.Font(self.font, self.size)
        
    def display(self, x, y, display):
        self.text = self.textfont.render(self.text, True, (255, 255, 255))
        display.blit(self.text, (x, y))