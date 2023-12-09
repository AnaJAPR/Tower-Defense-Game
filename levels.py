import pygame
import random
from constants import HEALTH, MONEY, SCREEN_WIDTH, SCREEN_HEIGHT
from game.load_enemy import ENEMY_SPAWN_DATA

class Level():
    def __init__(self, map_image:str, waypoints:list):
        self.level = 1
        self.spawned_enemies = 0
        self.enemy_list = []
        self.__map_image = pygame.image.load(map_image)
        self._health = HEALTH
        self.__initial_money = MONEY
        self._money =  self.__initial_money
        self.__waypoints = waypoints
        self.killed_enemies = 0
        self.lose_game = False

    def transform_image_proportions(self, width:int, height:int):
        self.__map_image = pygame.transform.scale(self.__map_image, (width, height))

    def draw_map(self, surface):
        surface.blit(self.__map_image, (0, 0))

    @property
    def initial_money(self):
        return self.__initial_money
    
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

    def clear_level_data(self):
        self.spawned_enemies = 0
        self.enemy_list = []
        self._health = HEALTH
        self._money =  self.__initial_money
        self.killed_enemies = 0

    def end_game(self, screen, enemy_group, turret_group, result_game):
        for enemy in enemy_group:
            enemy.kill()
        for turret in turret_group:
            turret.kill()
        self.clear_level_data()
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT + 300))
        image = pygame.image.load(f"assets\others\{result_game}.png").convert_alpha()
        image = pygame.transform.scale(image, (800, 380))
        screen.blit(image, (0, 0))
        


        # if result_game == "victory":

        

    # def lose_game(self, surface):
    #     if self._health <= 0:
    #         pygame.draw.rect(surface, (255,255,255), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
