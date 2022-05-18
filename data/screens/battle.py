import pygame
from data.handlers import fonthandler

def update(display):
    text = fonthandler.Font("data/fonts/DeterminationMono.TTF", 16, "placeholder until battle works. press ESCAPE to go back")
    
    text.display(0, 0, display)