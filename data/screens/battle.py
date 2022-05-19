import pygame
from data.handlers import fonthandler

class Battle():
    def __init__(self, display):
        self.display = display

def update(display):
    text = fonthandler.Font("data/fonts/DeterminationMono.TTF", 16, "placeholder until battle works. press ESCAPE to go back")
    
    text.display(0, 0, display)