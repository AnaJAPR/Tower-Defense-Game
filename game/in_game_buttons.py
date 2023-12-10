from buttons import Button, TwoActionButton
import constants as c

# Pause Menu Buttons
pause_button = TwoActionButton(745, 10, "assets/buttons/continue.png", "assets/buttons/pause.png")
pause_button.transform_image_proportions(50, 50)

# Restart Button
restart_button = Button(745, 65, "assets/buttons/restart.png")
restart_button.transform_image_proportions(50, 50)

# Game Over Restart Button
restart_game_over = Button(250, 475, "assets/buttons/newgame.png")
restart_game_over.transform_image_proportions(300, 100)

# Game Exit Restart Button
exit_game_over = Button(250, 575, "assets/buttons/menu.png")
exit_game_over.transform_image_proportions(300, 100)

# Exit Button
exit_button = Button(745, 120, "assets/buttons/exit.png")
exit_button.transform_image_proportions(50, 50)

# Add Turret Buttons
laser_button = Button(20, c.SCREEN_HEIGHT + 15, "assets/buttons/laser.png")
laser_button.transform_image_proportions(50, 50)

artillery_button = Button(120, c.SCREEN_HEIGHT + 15, "assets/buttons/artillery.png")
artillery_button.transform_image_proportions(50, 50)

# Remove Turret Button
rm_turret_button = Button(220, c.SCREEN_HEIGHT + 15, "assets/buttons/remove.png")
rm_turret_button.transform_image_proportions(50, 50)

# Upgrade Turret Button
upgrade_button = Button(320, c.SCREEN_HEIGHT + 15, "assets/buttons/up.png")
upgrade_button.transform_image_proportions(50, 50)

# Fast Forward Button
fast_forward_button = TwoActionButton(745, c.SCREEN_HEIGHT + 15, "assets/buttons/fast_forward.png", "assets/buttons/fast_forward_active.png")
fast_forward_button.transform_image_proportions(50, 50)
