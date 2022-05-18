import pygame
from data.handlers import fonthandler

def update(madeby, enemyname, showenemyname, display):
    title = fonthandler.Font("data/fonts/DeterminationMono.TTF", 48, "Undertale.py")

    bottomtext = fonthandler.Font("data/fonts/DeterminationMono.TTF", 16, f"Engine made by Aftermathic, Mod made by {madeby}")

    intruction_text = fonthandler.Font("data/fonts/DeterminationMono.TTF", 36, "Press Z to Start.")
    
    title.display(180, 10, display)
    bottomtext.display(5, 455, display)

    intruction_text.display(180, 380, display)
    
    if showenemyname:
        fight_text = fonthandler.Font("data/fonts/DeterminationMono.TTF", 16, f"VS {enemyname} Battle")
        fight_text.display(180, 3, display)