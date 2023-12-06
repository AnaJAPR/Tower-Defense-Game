import sys
sys.path.append('.')
import pygame
from game import waypoints as wp
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import levels as l

map = l.Map("assets/maps/map_1.png", wp.lvl1_waypoints)
map.transform_image_proportions(SCREEN_WIDTH, SCREEN_HEIGHT)