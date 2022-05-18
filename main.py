#Imports
from pypresence import Presence
from data.screens import battle, gameover, titlescr

import settings
import os

import pygame

#Disable Pygame Startup text
if not settings.pygame_starttext:
    os.system("clear")

#####################################################

#Discord Rich Presence

discord_found = False

try:
    test = Presence("975454058477396060")
    test.connect()
except:
    if settings.show_messages:
        print("Discord wasn't found in the computer.")
    discord_found = False
else:
    discord_found = True

    del test
    
    rpc = Presence("975454058477396060")
    rpc.connect()

####################################################

#game values
        
fps = 60
clock = pygame.time.Clock()

window_res = (640, 480)
window = pygame.display.set_mode(window_res)
pygame.display.set_caption("Undertale.py")

current_screen = 0

####################################################

#Event Loop

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if current_screen == 0:
        titlescr.update(settings.mod_creator, settings.titlescr_enemyname, settings.show_enemyname, window)

        if keys[pygame.K_z]:
            current_screen = 1

        if discord_found:
            rpc.update(state="In titlescreen")
            
    elif current_screen == 1:
        battle.update(window)

        if keys[pygame.K_ESCAPE]:
            current_screen = 0
            
        if discord_found:
            rpc.update(state="In a battle")
            
    else:
        if settings.show_messages:
            print("You might have been sent to a invalid screen.")
            
        if discord_found:
            rpc.update(state="In an invalid screen.")
                
    clock.tick(fps)
    pygame.display.update()

####################################################

#Exits game
pygame.quit()