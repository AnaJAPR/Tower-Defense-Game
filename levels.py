import pygame

class Map():
    def __init__(self, map_image:str, waypoints:list):
        self.map_image = pygame.image.load(map_image)
        self.waypoints = waypoints

    def transform_image_proportions(self, width:int, height:int):
        self.map_image = pygame.transform.scale(self.map_image, (width, height))

    def draw_map(self, surface):
        surface.blit(self.map_image, (0, 0))