import sys
sys.path.append('.')
import pygame
import constants as c
from turret import Turret

# Defining video mode
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

#individual turret image for mouse cursor
cursor_turret = pygame.image.load("assets/towers/Purple/Weapons/turret_01_mk1.png").convert_alpha()

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
    turret_group.add(turret)
        
# Creating turret group
turret_group = pygame.sprite.Group()