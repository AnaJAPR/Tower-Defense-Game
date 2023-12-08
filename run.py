import sys
sys.path.append('.')
import pygame
# from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
import constants as c
from enemy import Enemy
from turret import Turret
from game import load_maps as lm
from game import load_turrets as lt
from game import load_enemy as le
from game import in_game_buttons as igb

# Starting Pygame
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Setting the Screen Information
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT + c.BOTTOM_PANEL))
pygame.display.set_caption("Tower Defense Game")
# Game Variable
placing_turrets = False
selected_turret = None

# Loop
running = True
while running:

    clock.tick(c.FPS)

    # Inserting the map on the screen
    lm.map.draw_map(screen)

    # Update groups
    le.enemy_group.update()
    lt.turret_group.update(le.enemy_group)

    # Highlight selected turret
    if selected_turret:
        selected_turret.selected = True

    # Creating the button to add turrets and cancel the action
    if igb.turret_button.draw_button(screen):
        placing_turrets = not placing_turrets

    # Drawing Groups
    le.enemy_group.draw(screen)
    for turret in lt.turret_group:
        turret.draw(screen)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
            # mouse click
            mouse_pos = pygame.mouse.get_pos()
            #check if mouse is on the game area
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                #clear selected turrets
                selected_turret = None
                lt.clear_selection()
                if placing_turrets == True:
                    print("tap 2")
                    lt.create_turret(mouse_pos)
                else:
                    selected_turret = lt.select_turret(mouse_pos)
    
        # Press ESC to leave
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False

    # Display Update
    pygame.display.flip()

pygame.quit()