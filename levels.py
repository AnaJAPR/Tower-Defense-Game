import pygame
import random
from constants import HEALTH, MONEY, SCREEN_WIDTH, SCREEN_HEIGHT
from game.load_enemy import ENEMY_SPAWN_DATA

class Level():
    """
    Represents the game level with its mechanics.

    Parameters
    ---------- 
    map_image : str
        The file path to the file where the image is.
    waypoints : list
        A list of tuples representing the x and y coordinates of the points the enemies
        must walk through.
    
    Attributes
    ----------
    level : int
        The current level of the game.
    spawned_enemies : int
        Amount of enemies that have been spawned.
    enemy_list : list
        List of the enemies that have been spawned.
    __map_image : pygame.surface
        An image of the map loaded using pygame.
    _health : int
        The player's health.
    __initial_money : int
        The initial amount of money the player has.
    _money : int
        The current amount of money the player has.
    _waypoints : list
        A list of points defining the path that the enemies must follow.
    killed_enemies : int
        The amount of enemies that were killed during the level.

    Example
    -------
    level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
    """
    def __init__(self, map_image:str, waypoints:list):
        """
        Initialize a new instance of the Level class.   
        
        Parameters
        ---------- 
        map_image : str
            The file path to the file where the image is.
        waypoints : list
            A list of tuples representing the x and y coordinates of the points the enemies
            must walk through.
        """
        self.level = 1
        self.spawned_enemies = 0
        self.enemy_list = []
        self.__map_image = pygame.image.load(map_image)
        self.__initial_health = HEALTH
        self._health = self.__initial_health 
        self.__initial_money = MONEY
        self._money =  self.__initial_money
        self.__waypoints = waypoints
        self.killed_enemies = 0
        self.lose_game = False
        self.last_wave_spawn = pygame.time.get_ticks()
        self.n_waves = len(ENEMY_SPAWN_DATA)

    def transform_image_proportions(self, width:int, height:int):
        """
        Transform the image proportions to a specified width and height using Pygame's
        transform.scale function.

        Parameters
        ---------- 
        width: int
            The desired width of the image.
        height: int
            The desired height of the image.

        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        level.transform_image_proportions(69, 42)
        """
        self.__map_image = pygame.transform.scale(self.__map_image, (width, height))

    def draw_map(self, surface):
        """
        Draw the map on the specified surface.

        Parameters
        ---------- 
        surface : pygame.surface.Surface
            The surface on which the map will be drawn.
        
        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        level.draw_map(screen)
        """
        surface.blit(self.__map_image, (0, 0))

    @property
    def initial_health(self):
        """
        Get the initial health the player has.
        
        Returns
        -------
        int
            The initial health the player has
        
        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        initial_health = level.initial_health
        """
        return self.__initial_health   

    @property
    def initial_money(self):
        """
        Get the initial amount of money the player has.
        
        Returns
        -------
        int
            The initial amount of money the player has
        
        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        initial_money = level.initial_money
        """
        return self.__initial_money
    
    @property
    def money(self):
        """
        Get the current amount of money the player has.
        
        Returns
        -------
        int
            The current amount of money the player has
        
        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        initial_money = level.money
        """
        return self._money

    @money.setter
    def money(self, money):
        """
        Set the current amount of money the player has.

        Parameters
        ----------
        money : int
            The updated amount of money of the player

        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        level.money = 500
        """
        self._money = money

    @property
    def health(self):
        """
        Get the current health the player has.
        
        Returns
        -------
        int
            The current health the player has
        
        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        health = level.health
        """
        return self._health

    @health.setter
    def health(self, health):
        """
        Set the current health the player has.

        Parameters
        ----------
        health : int
            The updated health of the player

        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        level.health = 25
        """
        self._health = health

    def spawn_enemies(self):
        """
        Spawn enemies on the map according to some level attributes.

        Parameters
        ---------- 
        None

        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        level.spawn_enemies()
        """
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        #now randomize the list to shuffle the enemies
        random.shuffle(self.enemy_list)

    def clear_level_data(self):
        """
        Reset all the game mechanics to their initial status.

        Parameters
        ---------- 
        None
        
        Example
        -------
        level = Level("assets/maps/map_1.png", [(0, 0), (40, 60), (100, 100)])
        level.clear_level_data()
        """
        self.spawned_enemies = 0
        self.enemy_list = []
        self._health = HEALTH
        self._money =  self.__initial_money
        self.killed_enemies = 0
        self.level = 1

    def game_over(self, screen, enemy_group, turret_group, result_game):
        for enemy in enemy_group:
            enemy.kill()
        for turret in turret_group:
            turret.kill()

        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT + 300))
        image = pygame.image.load(f"assets\others\{result_game}.png").convert_alpha()
        image = pygame.transform.scale(image, (800, 380))
        screen.blit(image, (0, 0))
        
        if result_game == "victory":
            if self._health == self.__initial_health:
                star = pygame.image.load("assets\others\star.png").convert_alpha()
                star = pygame.transform.scale(star, (150, 150))
                screen.blit(star, (175, 325))
                screen.blit(star, (475, 325))
                screen.blit(star, (325, 325))

            if self._health >= self.__initial_health / 2 and self._health < self.__initial_health:
                star = pygame.image.load("assets\others\star.png").convert_alpha()
                star = pygame.transform.scale(star, (150, 150))
                screen.blit(star, (250, 325))
                screen.blit(star, (400, 325))
            
            if self._health < self.__initial_health / 2 :
                star = pygame.image.load("assets\others\star.png").convert_alpha()
                star = pygame.transform.scale(star, (150, 150))
                screen.blit(star, (325, 325))

# class SpawnEnemies(Level):
#     def __init__(self, map_image: str, waypoints: list):
#         super().__init__(map_image, waypoints)
    def spawn_waves(self):
        for wave in range(self.n_waves):
            self.spawn_enemies()
            self.level += 1
            self.last_wave_spawn = pygame.time.get_ticks()

    def process_enemies(self):
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        #now rando the list to shuffle enemies
        random.shuffle(self.enemy_list)
