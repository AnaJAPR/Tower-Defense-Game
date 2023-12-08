import pygame
import constants as c

class Map():
    def __init__(self, map_image:str, waypoints:list):
        self.__map_image = pygame.image.load(map_image)
        self._health = c.HEALTH
        self._money =  c.MONEY
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