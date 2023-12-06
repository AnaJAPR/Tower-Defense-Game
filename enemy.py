import pygame
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3

        self.waypoints = waypoints
        self.target_wp = 1

        self.position = Vector2(self.waypoints[0])
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # Method to make the enemy move
    def move(self):
        # Defining the target and the movement
        if self.target_wp < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_wp])
            self.movement = self.target - self.position
        # If there are no more waypoints to go, the enemy disappears
        else:
            self.kill()

        distance = self.movement.length()
        # If the distance to the next waypoint is greater than the enemy's speed, it will move at its natural speed
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            # While the distance is less than the enemy speed, the movement speed is equal to the distance
            if distance != 0:
                self.position += self.movement.normalize() * distance
            # Once the distance gets to 0, the next waypoint becomes into the new target
            self.target_wp += 1

        self.rect.center = self.position