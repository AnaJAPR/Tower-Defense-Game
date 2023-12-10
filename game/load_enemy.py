import pygame

# loading Enemies
enemy_1_image = pygame.image.load("assets/enemies/enemy_1.png")
enemy_2_image = pygame.image.load("assets/enemies/enemy_2.png")
enemy_3_image = pygame.image.load("assets/enemies/enemy_3.png")
enemy_4_image = pygame.image.load("assets/enemies/enemy_4.png")

# Groups
enemy_group = pygame.sprite.Group()

ENEMY_IMAGES ={
    "cadet"   : enemy_1_image,
    "officer" : enemy_2_image,
    "captain" : enemy_3_image,
    "general" : enemy_4_image
}

ENEMY_SPAWN_DATA = [
    #1
    {"cadet" : 10, "officer" : 0, "captain" : 0, "general" : 0},
    #2
    {"cadet" : 20, "officer" : 0, "captain" : 0, "general" : 0},
    #3
    {"cadet" : 25, "officer" : 5, "captain" : 0, "general" : 0},
    #4
    {"cadet" : 35, "officer" : 18, "captain" : 0, "general" : 0},
    #5
    {"cadet" : 20, "officer" : 20, "captain" : 5, "general" : 0},
    #6
    {"cadet" : 10, "officer" : 20, "captain" : 14, "general" : 0},
    #7
    {"cadet" : 1, "officer" : 102, "captain" : 0, "general" : 0},
    #8
    {"cadet" : 0, "officer" : 15, "captain" : 10, "general" : 5},
    #9
    {"cadet" : 0, "officer" : 50, "captain" : 23, "general" : 0},
    #10
    {"cadet" : 29, "officer" : 25, "captain" : 10, "general" : 9},
]

ENEMY_DATA = {
    "cadet"   : {"speed" : 1, "health": 5, "reward" : 10},
    "officer" : {"speed" : 2, "health": 10, "reward" : 10},
    "captain" : {"speed" : 4, "health": 15, "reward" : 10},
    "general" : {"speed" : 8, "health": 20, "reward" : 10}
}