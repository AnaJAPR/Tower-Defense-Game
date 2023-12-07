import pygame
import sys
import subprocess

class Button:
    def __init__(self, text, x, y, width, height, action=None):
        # Initialize a Button object with its position, size, text, and associated action
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (186, 147, 216)
        self.hover_color = (160, 110, 200)
        self.text = text
        self.action = action
        self.action_triggered = False

    def draw(self, screen):
        # Draw the button on the screen, change color when hovered, and execute action on click
        pygame.draw.rect(screen, self.color, self.rect)
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
            if mouse_click[0] == 1 and self.action is not None and not self.action_triggered:
                self.action()
                self.action_triggered = True

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Menu:
    def __init__(self, screen):
        # Initialize the menu with its associated screen and an empty list of buttons
        self.screen = screen
        self.buttons = []
        self.current_level = None
        self.original_background = pygame.image.load("menu_image.jpeg")
        self.background = self.original_background.copy()
        self.background_rect = self.background.get_rect()

    def add_button(self, button):
        # Add a button to the list of buttons in the menu
        self.buttons.append(button)

    def handle_events(self):
        # Handle various events including quitting, key presses, and mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Tecla Escape pressionada")
                    return 

            if event.type == pygame.VIDEORESIZE:
                self.handle_resize(event)

            for button in self.buttons:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button.rect.collidepoint(event.pos) and not button.action_triggered:
                    if button.text == "Start":
                        self.show_level_buttons() 
                    else:
                        button.action()
                        button.action_triggered = True
        
            # Update the position and size of the background image
            self.background_rect = self.background.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def handle_resize(self, event):
        # Resize the screen and update button positions to remain centered
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        for i, button in enumerate(self.buttons):
            button.rect.x = SCREEN_WIDTH // 2 - button.rect.width // 2
            button.rect.y = SCREEN_HEIGHT // 2 - len(self.buttons) * 25 + i * 50
        
        # Update the position and size of the background image while maintaining the original aspect ratio
        self.background = pygame.transform.scale(self.original_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_rect = self.background.get_rect()
        
    # Main loop for handling events and updating the screen
    def run(self):
        while True:
            self.handle_events()
            self.screen.blit(self.background, self.background_rect)  # Draw the image
    
            for button in self.buttons:
                button.draw(self.screen)

            pygame.display.flip()
            
            if self.current_level:
                self.start_game()
                self.current_level = None
    
    def show_level_buttons(self):
        self.buttons.clear()
        
        easy_button = Button("Easy", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 75, 200, 50, self.level_easy)
        medium_button = Button("Medium", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50, self.level_medium)
        hard_button = Button("Hard", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 25, 200, 50, self.level_hard)
        come_back_button = Button("Come Back", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 75, 200, 50, self.show_main_menu)

        menu.add_button(easy_button)
        menu.add_button(medium_button)
        menu.add_button(hard_button)
        menu.add_button(come_back_button)
        
    def create_main_menu_buttons(self):
        start_button = Button("Start", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 75, 200, 50, self.show_level_buttons)
        options_button = Button("Options", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50, self.show_options)
        almanac_button = Button("Almanac", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 25, 200, 50, self.show_almanac)
        game_story_button = Button("Game's story", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 75, 200, 50, self.game_story)
        help_button = Button("Help", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 125, 200, 50, self.show_help)

        self.add_button(start_button)
        self.add_button(options_button)
        self.add_button(almanac_button)
        self.add_button(game_story_button)
        self.add_button(help_button)

    def show_main_menu(self):
        self.buttons.clear()
        self.create_main_menu_buttons()
        self.run()

    def start_game(self):
        print("Starting the game...")
        
        if self.current_level:
            python_command = "python"
            script_path = "run.py"
            
            # Start the game in a new process
            subprocess.Popen([python_command, script_path])
        
            # Close the menu window
            pygame.quit()
            sys.exit()
            
            # Reset the menu after the game ends
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            pygame.display.set_caption("Tower Defense Menu")
            self.create_main_menu_buttons()

    def toggle_sound(self):
        print("Toggling sound...")

    def show_options(self):
        print("Showing options...")
    
    def show_almanac(self):
        print("Showing almanac...")
    
    def game_story(self):
        print("Telling the story of the game...")
    
    def show_help(self):
        print("displaying help...")
    
    def level_easy(self):
        print("Selected Easy level...")
        
        self.current_level = "Easy"

    def level_medium(self):
        print("Selected Medium level...")
        
        self.current_level = "Medium"

    def level_hard(self):
        print("Selected Hard level...")
        
        self.current_level = "Hard"

def main():
    pygame.init()

    # Screen settings
    global SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Tower Defense Menu")

    global menu 
    menu = Menu(screen)

    # Create buttons and add them to the menu
    menu.create_main_menu_buttons()

    menu.run()

if __name__ == "__main__":
    main()
