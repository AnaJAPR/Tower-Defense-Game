import sys
sys.path.append('.')
import pygame
import constants as c
from game import load_levels as ll
from game import load_enemy as le
from turret_data import TURRET_DATA
import math

class Turret(pygame.sprite.Sprite):
    def __init__(self, sprite_sheets, pos_x, pos_y, price):
        pygame.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.range = TURRET_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.upgrade_level - 1].get("cooldown")
        self.damage = TURRET_DATA[self.upgrade_level - 1].get("damage")
        self.last_shot = pygame.time.get_ticks()
        self.selected = False
        self.target = None
        self.price = price
        self.upgrade_price = self.price + 10

        #position variables
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        #animation variables
        self.sprite_sheets = sprite_sheets
        self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        #update image
        self.angle = 90
        self.original_image = self.animation_list[self.frame_index]
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

        #create range radius
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def load_images(self, sprite_sheet):
        #extracts images from spritesheet
        size = sprite_sheet.get_height()
        animation_list = []
        for x in range(c.ANIMATION_STEPS):
            temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_img)
        return animation_list
    
    def update(self, enemy_group):
        #if target picked, play firing animation
        if self.target:
            self.play_animation()
        else:
        #search for new target once turret has cooled down
            if pygame.time.get_ticks() - self.last_shot > self.cooldown:
                self.pick_target(le.enemy_group)
    
    def pick_target(self, enemy_group):
        #find an enemy to target
        x_dist = 0
        y_dist = 0
        #check distance to each enemy to see if it is in range
        for enemy in le.enemy_group:
            x_dist = enemy.position[0] - self.pos_x
            y_dist = enemy.position[1] - self.pos_y
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
                self.target = enemy
                self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                #deal damage to enemy
                self.target.health -= self.damage
                break

    def play_animation(self):
        #update image
        self.original_image = self.animation_list[self.frame_index]
        #check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            #check if animation has finished and reset to idle
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
                #record completed time and clear target so cooldown restarts
                self.last_shot = pygame.time.get_ticks()
                self.target = None
    
    def upgrade(self):        
        self.upgrade_level += 1
        self.range = TURRET_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.upgrade_level - 1].get("cooldown")
        self.damage = TURRET_DATA[self.upgrade_level - 1].get("damage")
        #upgrade turret image
        self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
        self.original_image = self.animation_list[self.frame_index]

        #upgrade range radius
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

    @property
    def sell(self):
        self.kill()
        ll.level.money += self.price + self.upgrade_price * (self.upgrade_level - 1)
