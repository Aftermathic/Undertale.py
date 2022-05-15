#Imports
from pypresence import Presence
from data import battle, errorscr, gameover, titlescr

import settings
import pygame
import os

#Startup###########################################

if not settings.pygame_starttext:
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    rpc = Presence("975454058477396060")
    rpc.connect()
except:
    if settings.debugging:
        print("Discord wasn't found in the computer.")

####################################################

#game values
fps = 60
clock = pygame.time.Clock()

window_res = (640, 480)
window = pygame.display.set_mode(window_res)
pygame.display.set_caption("Undertale.py")

real_width, real_height = pygame.display.get_surface().get_size()

game_running = True
while game_running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        window.fill((0, 0, 0))
        
        titlescr.update(window)
                
        clock.tick(fps)
        pygame.display.update()
        
    except Exception as e:
        print(e)
        
pygame.quit()