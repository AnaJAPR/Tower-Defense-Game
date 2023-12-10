import sys
sys.path.append('.')
import pygame
import constants as c
from turret import ArtilleryTurret, LaserTurret  # Assuming you have ArtilleryTurret and LaserTurret classes
from game import load_levels as ll
from game import load_sounds as ls
import math

# Defining video mode
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

# Individual turret image for mouse cursor
cursor_artillery = pygame.image.load("assets/towers/cursor_artillery.png").convert_alpha()
cursor_laser = pygame.image.load("assets/towers/cursor_laser.png").convert_alpha()

# Turret spritesheets
artillery_spritesheets = []
laser_spritesheets = []
for x in range(1, c.TURRET_LEVELS + 1):
    artillery_sheet = pygame.image.load(f"assets/towers/artillery_{x}.png").convert_alpha()
    laser_sheet = pygame.image.load(f"assets/towers/laser_{x}.png").convert_alpha()
    artillery_spritesheets.append(artillery_sheet)
    laser_spritesheets.append(laser_sheet)

def create_turret(mouse_pos, turret_type):
    """
    Create a turret at a determined position.

    Parameters
    ---------- 
    mouse_pos : tuple
        A tuple containing the x and y coordinates of the mouse
    turret_type : str
        The type of the turret: "artillery" or "laser".

    Returns
    -------
    bool
        The function always returns False

    Example
    -------
    create_turrets((20, 20), "artillery")
    """
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
    
    # Check if a turret already exists at the selected spot
    for existing_turret in turret_group:
        if existing_turret.pos_x == closest_base[0] and existing_turret.pos_y == closest_base[1]:
            return  # Do nothing if a turret already exists at the selected spot

    if min_distance <= max_placement_distance:
        if turret_type == 'artillery':
            new_turret = ArtilleryTurret(artillery_spritesheets, closest_base[0], closest_base[1], 200, ls.artillery_sfx)
        elif turret_type == 'laser':
            new_turret = LaserTurret(laser_spritesheets, closest_base[0], closest_base[1], 180, ls.laser_sfx)
            
        turret_group.add(new_turret)
        # Remove cost of turret
        ll.level.money -= new_turret.price
    
    return False

def select_turret(mouse_pos):
    """
    Select a turret using the mouse

    Parameters
    ---------- 
    mouse_pos : tuple
        A tuple containing the x and y coordinates of the mouse

    Returns
    -------
    None
        The function doesn't return anything.

    Example
    -------
    sekect_turret((50, 40))
    """

    for turret in turret_group:
        distance = math.sqrt((mouse_pos[0] - turret.pos_x)**2 + (mouse_pos[1] - turret.pos_y)**2)
        max_selection_distance = 50
        if distance <= max_selection_distance:
            return turret
    return None

def clear_selection():
    """
    Clear the towers selections.

    Example
    -------
    clear_selection()
    """
    for turret in turret_group:
        turret.selected = False
        
# Creating turret group
turret_group = pygame.sprite.Group()