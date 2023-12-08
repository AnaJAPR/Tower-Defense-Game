import sys
sys.path.append('.')
import pygame
from buttons import Button, TwoActionButton
import constants as c

# Add Turret Button
turret_button = Button(20, c.SCREEN_HEIGHT + 30, "assets/buttons/+.png")
turret_button.transform_image_proportions(69, 43)

# Upgrade Turret Button
upgrade_button = Button(120, c.SCREEN_HEIGHT + 30, "assets/buttons/up.png")
upgrade_button.transform_image_proportions(69, 43)

# Pause Menu Buttons
pause_button = TwoActionButton(520, c.SCREEN_HEIGHT + 30, "assets/buttons/pause.png", "assets/buttons/continue.png")
pause_button.transform_image_proportions(69, 43)