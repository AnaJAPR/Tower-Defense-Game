import pygame
import math
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image, speed):
        pygame.sprite.Sprite.__init__(self)
        self._speed = speed
        self._health = 1
        self._xp = 1

        self.__waypoints = waypoints
        self.__target_wp = 1

        self._position = Vector2(self.__waypoints[0])
        self.__angle = 0
        self._original_image = image
        self._image = pygame.transform.rotate(self._original_image, self.__angle)
        self.rect = self._image.get_rect()
        self.rect.center = self._position
    
    @property
    def position(self):
        return self._position

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        self._speed = speed

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

    def update(self):
        self.move()
        self.rotate()

    # Method to make the enemy move
    def move(self):
        # Defining the target and the movement
        if self.__target_wp < len(self.__waypoints):
            self.__target = Vector2(self.__waypoints[self.__target_wp])
            self.__movement = self.__target - self._position
        # If there are no more waypoints to go, the enemy disappears
        else:
            self.kill()

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
        self.rect = self._image.get_rect()
        self.rect.center = self._position