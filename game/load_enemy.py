import sys
sys.path.append('.')
import pygame
from enemy import Enemy
from game import waypoints as wp

# loading Enemies
enemy_1_image = pygame.image.load("assets/enemies/enemy_1.png")
enemy_2_image = pygame.image.load("assets/enemies/enemy_2.png")
enemy_3_image = pygame.image.load("assets/enemies/enemy_3.png")
enemy_4_image = pygame.image.load("assets/enemies/enemy_4.png")

# Groups
enemy_group = pygame.sprite.Group()

# Creating an Enemy
enemy_1 = Enemy(wp.lvl1_waypoints, enemy_1_image)
enemy_2 = Enemy(wp.lvl1_waypoints, enemy_2_image)
enemy_2.speed = 3
enemy_3 = Enemy(wp.lvl1_waypoints, enemy_3_image)
enemy_3.speed = 2
enemy_4 = Enemy(wp.lvl1_waypoints, enemy_4_image)
enemy_4.speed = 5

enemy_group.add(enemy_1)
enemy_group.add(enemy_2)
enemy_group.add(enemy_3)
enemy_group.add(enemy_4)