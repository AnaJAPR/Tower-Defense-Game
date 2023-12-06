import sys
sys.path.append('.')
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from enemy import Enemy
from turret import Turret
from game import load_maps as lm
from game import load_turrets as lt
from game import load_enemy as le

# Starting Pygame
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Setting the Screen Information
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Loop
running = True
while running:

    clock.tick(FPS)

    # Inserting the map on the screen
    screen.blit(lm.map, (0, 0))

    # Enemy movement
    le.enemy.move()

    # Drawing Groups
    le.enemy_group.draw(screen)
    lt.turret_group.draw(screen)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
            # mouse click
            mouse_pos = pygame.mouse.get_pos()
            turret = Turret(lt.cursor_turret, mouse_pos)
            lt.turret_group.add(turret)
    
        # Press ESC to leave
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False

    # Display Update
    pygame.display.flip()

pygame.quit()