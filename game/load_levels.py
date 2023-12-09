import pygame
from game.load_enemy import *
from game import waypoints as wp
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import levels

level = levels.Level("assets/maps/map_1.png", wp.lvl1_waypoints)
level.transform_image_proportions(SCREEN_WIDTH, SCREEN_HEIGHT)