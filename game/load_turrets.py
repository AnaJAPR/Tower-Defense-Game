import sys
sys.path.append('.')
import pygame
import constants as c
from turret import Turret
import math

# Defining video mode
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

#individual turret image for mouse cursor
cursor_turret = pygame.image.load("assets/towers/cursor_turret.png").convert_alpha()
#Turret spritesheets
turret_sheet = pygame.image.load("assets/towers/turret_01_mk1.png").convert_alpha()

def create_turret(mouse_pos):
    base_centers = [(392, 39),
                    (314, 185),
                    (472, 184),
                    (190, 261),
                    (427, 339),
                    (586, 411),
                    (711, 410),
                    (303, 482)]
    closest_base = None
    min_distance = float('inf')
    for base_center in base_centers:
        distance = math.sqrt((mouse_pos[0] - base_center[0])**2 + (mouse_pos[1] - base_center[1])**2)

        if distance < min_distance:
            min_distance = distance
            closest_base = base_center

    max_placement_distance = 50
    if min_distance <= max_placement_distance:
        new_turret = Turret(turret_sheet, closest_base[0], closest_base[1])
        turret_group.add(new_turret)

def select_turret(mouse_pos):
    for turret in turret_group:
        if (mouse_pos[0], mouse_pos[1]) == (turret.pos_x, turret.pos_y):
            return turret
        
def clear_selection():
   for turret in turret_group:
      turret.selected = False
        
# Creating turret group
turret_group = pygame.sprite.Group()