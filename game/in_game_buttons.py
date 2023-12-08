import sys
sys.path.append('.')
import pygame
from buttons import Button
import constants as c

# temp_screen = pygame.display.set_mode((800, 600))
# remove_turret_button = pygame.image.load("assets/buttons/-.png").convert_alpha()

turret_button = Button(20, c.SCREEN_HEIGHT + 30, "assets/buttons/+.png")
turret_button.transform_image_proportions(69, 43)

# cancel_button = Button(400, c.SCREEN_HEIGHT + 30, remove_turret_button)
# cancel_button.transform_image_proportions(69, 43)

upgrade_button = Button(120, c.SCREEN_HEIGHT + 30, "assets/buttons/up.png")
upgrade_button.transform_image_proportions(69, 43)