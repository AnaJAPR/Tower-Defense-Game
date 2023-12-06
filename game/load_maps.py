import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Loading Map
map = pygame.image.load("assets/maps/map_1.png")
map = pygame.transform.scale(map, (SCREEN_WIDTH, SCREEN_HEIGHT))