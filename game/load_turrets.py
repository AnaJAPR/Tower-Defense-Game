import pygame

# Defining video mode
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

#individual turret image for mouse cursor
cursor_turret = pygame.image.load("assets/towers/Purple/Weapons/turret_01_mk1.png").convert_alpha()

# Creating turret group
turret_group = pygame.sprite.Group()