import sys
sys.path.append('.')
import pygame
import constants as c
from turret import Turret

# Defining video mode
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

#individual turret image for mouse cursor
cursor_turret = pygame.image.load("assets/towers/cursor_turret.png").convert_alpha()
#Turret spritesheets
turret_sheet = pygame.image.load("assets/towers/turret_01_mk1.png").convert_alpha()

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    space_is_free = True
    for turret in turret_group:
       if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
           space_is_free = False
       if space_is_free == True:
        turret = Turret(turret_sheet, mouse_tile_x, mouse_tile_y)
        turret_group.add(turret)

def select_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    for turret in turret_group:
        if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
            return turret
        
# Creating turret group
turret_group = pygame.sprite.Group()