import pygame
import random
from constants import HEALTH, MONEY
from game.load_enemy import ENEMY_SPAWN_DATA

class Level():
    def __init__(self, map_image:str, waypoints:list):
        self.level = 1
        self.spawned_enemies = 0
        self.enemy_list = []
        self.__map_image = pygame.image.load(map_image)
        self._health = HEALTH
        self._money =  MONEY
        self.__waypoints = waypoints

    def transform_image_proportions(self, width:int, height:int):
        self.__map_image = pygame.transform.scale(self.__map_image, (width, height))

    def draw_map(self, surface):
        surface.blit(self.__map_image, (0, 0))

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    def spawn_enemies(self):
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        #now randomize the list to shuffle the enemies
        random.shuffle(self.enemy_list)