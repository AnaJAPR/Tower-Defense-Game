import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS

# Starting Pygame
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Map
map = pygame.image.load("assets\maps\map_1.png")
map = pygame.transform.scale(map, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Setting the Screen Information
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Loop
running = True
while running:

    clock.tick(FPS)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pressione ESC para sair
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False

    # Inserting the map on the screen
    screen.blit(map, (0, 0))

    pygame.display.flip()

pygame.quit()