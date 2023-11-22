"""
Input handling and collision detection practice
To implement: 
- Robust input handling system
- Collision detection between entities of different shape
- Scene handling
"""
import pygame
from globals import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    INPUT_STREAM.process_input()
    SCENE_MANAGER.input()
    # SCENE_MANAGER.update()
    SCENE_MANAGER.render()
    CLOCK.tick(60)

pygame.quit()