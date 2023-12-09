import pygame
# from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
import constants as c
from enemy import Enemy
from turret import Turret
from game import load_levels as ll
from game import load_turrets as lt
from game.load_levels import *
from game import in_game_buttons as igb

# Starting Pygame
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Setting the Screen Information
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT + c.BOTTOM_PANEL))
pygame.display.set_caption("Tower Defense Game")

text_font = pygame.font.SysFont("Consolas", 24, bold = True)
large_font = pygame.font.SysFont("Consolas", 36)

#function to show text on screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Game Variable
placing_turrets = False
selected_turret = None
is_paused = False
last_enemy_spawn = pygame.time.get_ticks()
removing_turrets = False

# Initializing spawn enemies proccess
ll.level.spawn_enemies()

# Loop
running = True
while running:

    clock.tick(c.FPS)
    
    # Menu Area
    screen.fill((126, 52, 0))

    # Inserting the map on the screen
    ll.level.draw_map(screen)

    # Update groups
    if not is_paused:
        enemy_group.update(screen)
        lt.turret_group.update(enemy_group)
    if is_paused:
        pass

    # Highlight selected turret
    if selected_turret:
        selected_turret.selected = True
    
    # Creating the button to add turrets and cancel the action
    if igb.turret_button.draw_button(screen):
        placing_turrets = not placing_turrets

    if igb.pause_button.draw_button(screen):
        is_paused = not is_paused

    if igb.rm_turret_button.draw_button(screen):
        removing_turrets = not removing_turrets

    if not is_paused:
        #if turret is selected, show upgrade button
        if selected_turret:
            #if turret can be upgraded, show upgrade button
            if selected_turret.upgrade_level < c.TURRET_LEVELS:
                if igb.upgrade_button.draw_button(screen):
                    if ll.level.money >= selected_turret.upgrade_price:
                        selected_turret.upgrade()
                        ll.level.money -= selected_turret.upgrade_price

        if pygame.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
            if level.spawned_enemies < len(level.enemy_list):
                enemy_type = level.enemy_list[level.spawned_enemies]
                enemy_image = ENEMY_IMAGES.get(enemy_type)
                enemy = Enemy(wp.lvl1_waypoints, enemy_image, enemy_type)
                enemy_group.add(enemy)
                level.spawned_enemies += 1
                last_enemy_spawn = pygame.time.get_ticks()


    # Drawing Groups
    enemy_group.draw(screen)
    for turret in lt.turret_group:
        turret.draw(screen)

    draw_text(str(ll.level.health), text_font, "grey100", 0, 0)
    draw_text(str(ll.level.money), text_font, "grey100", 0, 30)

    # Drawing a tower that follows the mouse
    if placing_turrets:
        cursor_rect = lt.cursor_turret.get_rect()
        cursor_pos = pygame.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[1] <= c.SCREEN_HEIGHT:
            screen.blit(lt.cursor_turret, cursor_rect)

    for event in pygame.event.get():

        if not is_paused:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
                # mouse click
                mouse_pos = pygame.mouse.get_pos()
                #check if mouse is on the game area
                if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                    #clear selected turrets
                    selected_turret = None
                    lt.clear_selection()
                    if placing_turrets == True:
                        #check if there is enough money
                        if ll.level.money >= c.BUY_COST:
                            placing_turrets = lt.create_turret(mouse_pos)
                    elif removing_turrets == True:
                        for turret in lt.turret_group:
                            turret.clicked() 
                    else:
                        selected_turret = lt.select_turret(mouse_pos)

        # Quit Event    
        if event.type == pygame.QUIT:
            running = False
        
        # Press ESC to leave
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False

    # Display Update
    pygame.display.flip()

pygame.quit()