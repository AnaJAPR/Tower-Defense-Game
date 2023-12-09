import pygame
import math
from pygame.math import Vector2
from game import load_levels as ll
from game.load_enemy import ENEMY_DATA

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image, enemy_type):
        pygame.sprite.Sprite.__init__(self)

        self._speed = ENEMY_DATA.get(enemy_type)["speed"]
        self._health = ENEMY_DATA.get(enemy_type)["health"]
        self.__initial_health = ENEMY_DATA.get(enemy_type)["health"]
        self._xp = ENEMY_DATA.get(enemy_type)["xp"]

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
        return self._position

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        self._health = health

    @property
    def xp(self):
        return self._xp
    
    @xp.setter
    def xp(self, xp):
        self._xp = xp

    def draw_health_bar(self, surface):
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

    def update(self, surface):
        self.move()
        self.rotate()
        self.check_alive()
        self.draw_health_bar(surface)

    # Method to make the enemy move
    def move(self):
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
        #calculate distance to next waypoint
        dist = self.__target - self._position
        #use distance to calculate angle
        self.__angle = math.degrees(math.atan2(-dist[1], dist[0]))
        #rotate image and update rectangle
        self.image = pygame.transform.rotate(self._original_image, self.__angle)
        self.rect = self.image.get_rect()
        self.rect.center = self._position

    def check_alive(self):
        if self._health <= 0:
            self.kill()
            ll.level.money += self._xp
