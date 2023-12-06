import sys
sys.path.append('.')
import pygame
from buttons import Button
import constants as c

new_turret_button = pygame.image.load("assets/buttons/+.png").convert_alpha()
remove_turret_button = pygame.image.load("assets/buttons/-.png").convert_alpha()

turret_button = Button(20, c.SCREEN_HEIGHT + 30, new_turret_button)
cancel_button = Button(400, c.SCREEN_HEIGHT + 30, remove_turret_button)
 
turret_button.transform_image_proportions(69, 43)
cancel_button.transform_image_proportions(69, 43)