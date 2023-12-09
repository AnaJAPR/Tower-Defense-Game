import pygame

# loading Enemies
enemy_1_image = pygame.image.load("assets/enemies/enemy_1.png")
enemy_2_image = pygame.image.load("assets/enemies/enemy_2.png")
enemy_3_image = pygame.image.load("assets/enemies/enemy_3.png")
enemy_4_image = pygame.image.load("assets/enemies/enemy_4.png")

# Groups
enemy_group = pygame.sprite.Group()

ENEMY_IMAGES ={
    "enemy_1" : enemy_1_image,
    "enemy_2" : enemy_2_image,
    "enemy_3" : enemy_3_image,
    "enemy_4" : enemy_4_image
}

ENEMY_SPAWN_DATA = [
    {"enemy_1" : 15, "enemy_2" : 15, "enemy_3" : 10, "enemy_4" : 2}
]
ENEMY_DATA = {
    "enemy_1" : {"speed" : 2, "health": 7, "xp" : 40},
    "enemy_2" : {"speed" : 3, "health": 5, "xp" : 60},
    "enemy_3" : {"speed" : 1, "health": 10, "xp" : 30},
    "enemy_4" : {"speed" : 5, "health": 1, "xp" : 20}
}