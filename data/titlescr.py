import pygame
from data.handlers import fonthandler

def update(display):
    #you need the full path
    title = fonthandler.Font("data/fonts/DeterminationMono.TTF", 32, "Undertale.py")
    title.display(0, 0, display)