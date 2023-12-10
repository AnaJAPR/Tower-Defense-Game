import pygame
import math
from pygame.math import Vector2
from game import load_levels as ll
from game.load_enemy import ENEMY_DATA

class Enemy(pygame.sprite.Sprite):
    """
    Represents the enemy and its mechanics.

    Parameters
    ---------- 
    waypoints : list
        A list of tuples representing the x and y coordinates of the points the enemies
        must walk through.
    image : pygame.surface.Surface
        An image loaded using Pygame.
    enemy_type : str
        A string saying what's the type of the enemy.    
    
    Attributes
    ----------
    _speed : float
        Enemy's speed obtained from the ENEMY_DATA dictionary.
    _health : int
        Enemy's health obtained from the ENEMY_DATA dictionary.
    __initial_health : int
        Enemy's initial health obtained from the ENEMY_DATA dictionary.
    _reward : int
        Amount of money earned by the player when an enemy is killed. Obtained from the
        ENEMY_DATA dictionary.
    _waypoints : list
        A list of tuples representing the x and y coordinates of the points the enemies
        must walk through.
    _target_wp : int
        Index of the waypoints list that the enemy is currently going to.
    _position : pygame.math.Vector2
        Current position of the enemy.
    __angle : int
        Angle that the enemy must turn while walking
    _original_image : pygame.surface.Surface
        An image loaded using Pygame.
    image : pygame.surface.Surface
        Original image after being rotated.
    rect : pygame.rect.Rect
        Rect where the enemy's image is drawn.
    rect.center : tuple 
        Coordinates x and y for the center of the rect.

    Example
    -------
    enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
    """
    def __init__(self, waypoints, image, enemy_type):
        """
        Initialize a new instance of the Enemy class.

        Parameters
        ---------- 
        waypoints : list
            A list of tuples representing the x and y coordinates of the points the enemies
            must walk through.
        image : pygame.surface.Surface
            An image loaded using Pygame.
        enemy_type : str
            A string saying what's the type of the enemy.            
        """
        pygame.sprite.Sprite.__init__(self)

        self._speed = ENEMY_DATA.get(enemy_type)["speed"]
        self._health = ENEMY_DATA.get(enemy_type)["health"]
        self.__initial_health = ENEMY_DATA.get(enemy_type)["health"]
        self._reward = ENEMY_DATA.get(enemy_type)["reward"]

        self.__waypoints = waypoints
        self.__target_wp = 1

        self._position = Vector2(self.__waypoints[0])
        self.__angle = 0
        self._original_image = image
        self.image = pygame.transform.rotate(self._original_image, self.__angle)
        self.rect = self.image.get_rect()
        self.rect.center = self._position
    
    @property
    def position(self):
        """
        Get the current position of the enemy.
        
        Returns
        -------
        pygame.math.Vector2
            The current position of the enemy.
        
        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.position
        """
        return self._position

    @property
    def health(self):
        """
        Get the current health of the enemy.
        
        Returns
        -------
        int
            The current health of the enemy.
        
        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.health
        """
        return self._health
    
    @health.setter
    def health(self, health):
        """
        Set the current amount of health the enemy has.

        Parameters
        ----------
        money : int
            The updated amount of health of the enemy

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.health = 20
        """
        self._health = health

    @property
    def reward(self):
        """
        Get how much money the player will earn if the enemy get killed.
        
        Returns
        -------
        int
            The amount of the money the player will earn.
        
        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.reward
        """
        return self._reward
    
    @reward.setter
    def reward(self, reward):
        """
        Set the amount of money the player will earn killing the enemy.

        Parameters
        ----------
        money : int
            The updated amount of money the enemy will give.

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.reward = 20
        """
        self._reward = reward

    def draw_health_bar(self, surface):
        """
        Draw the health bar on the specified surface.

        Parameters
        ---------- 
        surface : pygame.surface.Surface
            The surface on which the enemy's health bar will be drawn.

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.draw_health_bar(screen)
        """
        bar_width = 25
        bar_height = 5

        # Calculates current life as a percentage of total life
        pct = self._health / self.__initial_health

        # Normalizing
        if pct > 1: 
            pct = 1

        # Set the health bar position
        pos_x = self._position[0] - bar_width / 2
        pos_y = self._position[1] - 30

        # Draw the life bar
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(pos_x, pos_y, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(pos_x, pos_y, bar_width * pct, bar_height))

    # Method to make the enemy move
    def move(self):
        """
        Causes the enemy to walk through the waypoints.

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.move()
        """
        # Defining the target and the movement
        if self.__target_wp < len(self.__waypoints):
            self.__target = Vector2(self.__waypoints[self.__target_wp])
            self.__movement = self.__target - self._position
        # If there are no more waypoints to go, the enemy disappears
        else:
            self.kill()
            ll.level.health -= self.__initial_health

        distance = self.__movement.length()
        # If the distance to the next waypoint is greater than the enemy's speed, it will move at its natural speed
        if distance >= self._speed:
            self._position += self.__movement.normalize() * self._speed
        else:
            # While the distance is less than the enemy speed, the movement speed is equal to the distance
            if distance != 0:
                self._position += self.__movement.normalize() * distance
            # Once the distance gets to 0, the next waypoint becomes into the new target
            self.__target_wp += 1

        self.rect.center = self._position
    
    def rotate(self):
        """
        Causes the enemy to rotate so that they are always looking in the direction 
        they are going

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.rotate()
        """
        #calculate distance to next waypoint
        dist = self.__target - self._position
        #use distance to calculate angle
        self.__angle = math.degrees(math.atan2(-dist[1], dist[0]))
        #rotate image and update rectangle
        self.image = pygame.transform.rotate(self._original_image, self.__angle)
        self.rect = self.image.get_rect()
        self.rect.center = self._position

    def check_alive(self):
        """
        Checks if the enemy is still alive, and if not, makes the enemy disappear.

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.check_alive()
        """
        if self._health <= 0:
            self.kill()
            ll.level.money += self._reward
            ll.level.killed_enemies += 1

    def update(self, surface):
        """
        Updates the enemy, making it move and rotate, checking if it's still alive and
        drawing its health bar.

        Example
        -------
        enemy = Enemy([(0, 0), (10, 10, (20, 20))], "assets\enemies\enemy_1.png", "enemy_1")
        enemy.rotate()
        """
        self.move()
        self.rotate()
        self.check_alive()
        self.draw_health_bar(surface)