import sys
sys.path.append('.')
import pygame
from enemy import Enemy
from game import waypoints as wp

# loading Enemies
enemy_image = pygame.image.load("assets/enemies/enemy.png")

# Groups
enemy_group = pygame.sprite.Group()

# Creating an Enemy
enemy = Enemy(wp.lvl1_waypoints, enemy_image)
enemy_group.add(enemy)