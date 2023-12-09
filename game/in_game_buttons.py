import sys
sys.path.append('.')
import pygame
from buttons import Button, TwoActionButton
import constants as c

# Pause Menu Buttons
pause_button = TwoActionButton(726, 5, "assets/buttons/continue.png", "assets/buttons/pause.png")
pause_button.transform_image_proportions(69, 42)

# Restart Button
restart_button = Button(726, 52, "assets/buttons/restart.png")
restart_button.transform_image_proportions(69, 42)

# Game Over Restart Button
restart_game_over = Button(250, 450, "assets/buttons/restart.png")
restart_game_over.transform_image_proportions(300, 80)

# Game Exit Restart Button
exit_game_over = Button(250, 540, "assets/buttons/exit.png")
exit_game_over.transform_image_proportions(300, 80)

# Exit Button
exit_button = Button(726, 99, "assets/buttons/exit.png")
exit_button.transform_image_proportions(69, 42)

# Add Turret Button
turret_button = Button(20, c.SCREEN_HEIGHT + 30, "assets/buttons/+.png")
turret_button.transform_image_proportions(69, 42)

# Remove Turret Button
rm_turret_button = Button(120, c.SCREEN_HEIGHT + 30, 'assets/buttons/-.png')
rm_turret_button.transform_image_proportions(69, 42)

# Upgrade Turret Button
upgrade_button = Button(220, c.SCREEN_HEIGHT + 30, "assets/buttons/up.png")
upgrade_button.transform_image_proportions(69, 42)
