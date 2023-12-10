import pygame
import sys
import constants as c
from enemy import Enemy
from game import load_turrets as lt
from game.load_levels import *
from game import in_game_buttons as igb
from game import load_others as lo
from game import load_sounds as ls
from menu import Menu

# Starting Pygame
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Setting the Screen Information
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT + c.BOTTOM_PANEL))
pygame.display.set_caption("Tower Defense Game")
ls.game_music.play(-1)

# Font of the Information on the screen
text_font = pygame.font.SysFont("Consolas", 24, bold=True)
large_font = pygame.font.SysFont("Consolas", 36)

# function to show text on screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def display_data():
    draw_text("LEVEL: " + str(level.level) + "/15", text_font, "grey100", 0, 0)
    screen.blit(lo.heart_image, (5, 30))
    draw_text(str(level.health), text_font, "grey100", 45, 30)
    screen.blit(lo.coin_image, (5, 60))
    draw_text(str(level.money), text_font, "grey100", 45, 60)


# GAME VARIABLES
# Game Moments
is_paused = True
is_starting = True
on_going = True

# Adding and Removing Turrets
placing_turrets = False
removing_turrets = False
selected_turret = None

# Spawning Enemies
last_enemy_spawn = pygame.time.get_ticks()

# Initializing spawn enemies process
level.spawn_enemies()

# Loop
running = True
while running:

    clock.tick(c.FPS)

    if on_going:
        # Menu Area
        screen.fill((126, 52, 0))

        # Inserting the map on the screen
        level.draw_map(screen)

        # UPDATE GROUPS
        # Updating Turrets
        if is_paused == False or is_starting == True:
            lt.turret_group.update(enemy_group)

        # Updating Enemies
        if is_paused == False:
            enemy_group.update(screen)

        # Highlight selected turret
        if selected_turret:
            selected_turret.selected = True

        # Creating the button to add artillery turrets and cancel the action
        if igb.artillery_button.draw_button(screen):
            placing_turrets = not placing_turrets
            removing_turrets = False
            selected_turret_type = "artillery"

        # Creating the button to add laser turrets and cancel the action
        if igb.laser_button.draw_button(screen):
            placing_turrets = not placing_turrets
            removing_turrets = False
            selected_turret_type = "laser"

        # Creating the button to remove turrets and cancel the action
        if igb.rm_turret_button.draw_button(screen):
            removing_turrets = not removing_turrets
            placing_turrets = False

        # Creating the pause button
        if igb.pause_button.draw_button(screen):
            is_paused = not is_paused
            is_starting = False

        # Restart the game
        if igb.restart_button.draw_button(screen):
            igb.pause_button.status = True
            is_starting = True
            is_paused = True
            for enemy in enemy_group:
                enemy.kill()
            for turret in lt.turret_group:
                turret.kill()
            level.clear_level_data()
            last_enemy_spawn = pygame.time.get_ticks()
            level.spawn_enemies()

        if igb.exit_button.draw_button(screen):
            Menu()

            sys.exit()

        # if turret is selected, show upgrade button
        if selected_turret:
            # if turret can be upgraded, show upgrade button
            if selected_turret.upgrade_level < c.TURRET_LEVELS:
                if igb.upgrade_button.draw_button(screen):
                    if level.money >= selected_turret.upgrade_price:
                        level.money -= selected_turret.upgrade_price
                        
                        selected_turret.upgrade()
        if not is_paused:
            # Fast Forward Option
            level.game_speed = 1
            igb.fast_forward_button.draw_button(screen)
            if igb.fast_forward_button.status == False:
                level.game_speed = 4
            # Spawning enemies
            if pygame.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
                if level.spawned_enemies < len(level.enemy_list):
                    enemy_type = level.enemy_list[level.spawned_enemies]
                    enemy_image = ENEMY_IMAGES.get(enemy_type)
                    enemy = Enemy(wp.lvl1_waypoints, enemy_image, enemy_type)
                    enemy_group.add(enemy)
                    level.spawned_enemies += 1
                    last_enemy_spawn = pygame.time.get_ticks()
                # Win Game
                else:
                    if not level.killed_enemies < level.spawned_enemies:
                        if level.level == level.n_waves:
                            is_starting = True
                            is_paused = True
                            on_going = False
                            level.game_over(screen, enemy_group, lt.turret_group, "victory")
                            level.clear_level_data()
                        else:
                            level.level += 1
                            level.spawn_enemies()
    
        # Lose game
        if level.health <= 0:
            is_starting = True
            is_paused = True
            on_going = False
            level.game_over(screen, enemy_group, lt.turret_group, "defeat")
            level.clear_level_data()
    
    # Add buttons to game over screens
    if not on_going:
        if igb.restart_game_over.draw_button(screen):
            on_going = True
            igb.pause_button.status = True
            is_starting = True
            is_paused = True
            level.clear_level_data()
            last_enemy_spawn = pygame.time.get_ticks()
            level.spawn_enemies()

        if igb.exit_game_over.draw_button(screen):
            Menu()
            sys.exit()

    # Drawing Groups
    enemy_group.draw(screen)

    for turret in lt.turret_group:
        turret.draw(screen)

    display_data()

    # Drawing a tower that follows the mouse
    if placing_turrets == True and removing_turrets == False:
        if selected_turret_type == "artillery":
            cursor_turret = lt.cursor_artillery
            cursor_rect = cursor_turret.get_rect()
            cursor_pos = pygame.mouse.get_pos()
            cursor_rect.center = cursor_pos
            if cursor_pos[1] <= c.SCREEN_HEIGHT:
                screen.blit(cursor_turret, cursor_rect)
                
        elif selected_turret_type == "laser":
            cursor_turret = lt.cursor_laser
            cursor_rect = cursor_turret.get_rect()
            cursor_pos = pygame.mouse.get_pos()
            cursor_rect.center = cursor_pos
            if cursor_pos[1] <= c.SCREEN_HEIGHT:
                screen.blit(cursor_turret, cursor_rect)

    # Drawing a X that follows the mouse
    if removing_turrets == True and placing_turrets == False:
        cursor_rect = lo.pointer_x.get_rect()
        cursor_pos = pygame.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[1] <= c.SCREEN_HEIGHT:
            screen.blit(lo.pointer_x, cursor_rect)

    for event in pygame.event.get():
        if is_paused == False or is_starting == True:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # mouse click
                mouse_pos = pygame.mouse.get_pos()
                # check if mouse is on the game area
                if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                    # clear selected turrets
                    selected_turret = None
                    lt.clear_selection()
                    # Check whether the placing turrets button is pressed or not
                    if placing_turrets == True and removing_turrets == False:
                        # check if there is enough money
                        if level.money >= c.BUY_COST:
                            # Put the turret
                            placing_turrets = lt.create_turret(mouse_pos, selected_turret_type)
                    # Check whether the removing turrets button is pressed or not
                    elif removing_turrets == True and placing_turrets == False:
                        for turret in lt.turret_group:
                            # Remove the turret
                            removing_turrets = turret.sell()
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