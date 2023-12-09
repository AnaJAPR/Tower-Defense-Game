import sys
sys.path.append('.')
import pygame
from buttons import Button, TwoActionButton  # Assuming you have TwoActionButton class
import constants as c

# Pause Menu Buttons
pause_button = TwoActionButton(726, 5, "assets/buttons/continue.png", "assets/buttons/pause.png")
pause_button.transform_image_proportions(69, 42)

# Restart Button
restart_button = Button(726, 52, "assets/buttons/restart.png")
restart_button.transform_image_proportions(69, 42)

# Exit Button
exit_button = Button(726, 99, "assets/buttons/exit.png")
exit_button.transform_image_proportions(69, 42)

# Add Turret Buttons
laser_button = Button(20, c.SCREEN_HEIGHT + 30, "assets/buttons/laser.png")
laser_button.transform_image_proportions(69, 43)

artillery_button = Button(120, c.SCREEN_HEIGHT + 30, 'assets/buttons/artillery.png')
artillery_button.transform_image_proportions(69, 43)

# Remove Turret Button
rm_turret_button = Button(220, c.SCREEN_HEIGHT + 30, 'assets/buttons/-.png')
rm_turret_button.transform_image_proportions(69, 43)

# Upgrade Turret Button
upgrade_button = Button(320, c.SCREEN_HEIGHT + 30, "assets/buttons/up.png")
upgrade_button.transform_image_proportions(69, 43)
