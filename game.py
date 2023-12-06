import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from enemy import Enemy
from turret import Turret

# Starting Pygame
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Loading Map
map = pygame.image.load("assets/maps/map_1.png")
map = pygame.transform.scale(map, (SCREEN_WIDTH, SCREEN_HEIGHT))

#individual turret image for mouse cursor
cursor_turret = pygame.image.load("assets/towers/Blue/Weapons/turret_01_mk1.gif").convert_alpha()

# loading Enemies
enemy_image = pygame.image.load("assets/enemies/enemy.png")

# Groups
enemy_group = pygame.sprite.Group()
turret_group = pygame.sprite.Group()

# Enemy waypoints
waypoints = [
    (0, 340), 
    (250, 340),
    (250, 110),
    (540, 110),
    (540, 260),
    (365, 260),
    (365, 485),
    (650, 485),
    (650, 330),
    (800, 330),
]

# Creating an Enemy
enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

# Setting the Screen Information
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Loop
running = True
while running:

    clock.tick(FPS)

    # Inserting the map on the screen
    screen.blit(map, (0, 0))

    # Enemy movement
    enemy.move()

    # Drawing Groups
    enemy_group.draw(screen)
    turret_group.draw(screen)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #mouse click
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = pg.mouse.get_pos()
        turret = Turret(cursor_turret, mouse_pos)
        turret_group.add(turret)
    
    # Pressione ESC para sair
    elif event.type == pygame.KEYDOWN:
        if event.type == pygame.K_ESCAPE:
            running = False

    # Display Update
    pygame.display.flip()

pygame.quit()