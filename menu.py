import pygame
import sys
import subprocess
import os

class Button:
    def __init__(self, image, pos, text_input, base_color, hovering_color):
        # Initialize a Button object with its position, size, text, and associated action
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = self.font.SysFont(None, 36)
        self.base_color, self.hovering_color = (186, 147, 216), (160, 110, 200)
        self.text_input = text_input
        self.font_size = 36
        self.font = pygame.font.SysFont(None, self.font_size)
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.rect)
        
    def checkForInput(self, position):
        return self.rect.collidepoint(position)
    
    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class Menu:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defense Menu")
        self.BG = pygame.image.load("assets/background_menu/menu_image.jpeg")
        self.run()
    
    def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill((0,0,0))

            PLAY_TEXT = pygame.font.Font(none, 36).render("This is the PLAY screen.", True, (255, 255, 255))
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill((255,255,255))

            OPTIONS_TEXT = pygame.font.Font(None, 36).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = pygame.font.Font(None, 36).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/buttons_images/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/buttons_images/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/buttons_images/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            
    def run(self):
        self.main_menu()

if __name__ == "__main__":
    menu = Menu()





'''
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
    def __init__(self, screen_width, screen_height):
        # Initialize the menu with its associated screen and an empty list of buttons
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.buttons = []
        self.original_buttons = []  # Store original buttons to preserve references
        self.current_level = None
        self.original_background = pygame.image.load("menu_image.jpeg")
        self.background = self.original_background.copy()
        self.background_rect = self.background.get_rect()
        self.running = True   # add the control variable
        self.level_buttons_shown = False
        self.selected_level = None

    def add_button(self, button):
        # Add a button to the list of buttons in the menu
        self.buttons.append(button)
        self.original_buttons.append(button)

    def handle_events(self):
        # Handle various events including quitting, key presses, and mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         print("Tecla Escape pressionada")
            #         return 
            

            if event.type == pygame.VIDEORESIZE:
                self.handle_resize(event)

            for button in self.buttons:
                if (event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == 1 
                    and button.rect.collidepoint(event.pos)
                    and not button.action_triggered):
                    if button.text == "Start":
                        self.show_level_buttons()
                    else:
                        button.action()
                        button.action_triggered = True

        # for button in self.buttons:
        #     button.action_triggered = False
            
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
        if not self.level_buttons_shown: # checks if the buttons are already displayed
            self.buttons.clear()
        
            easy_button = Button("Easy", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 75, 200, 50, self.level_easy)
            medium_button = Button("Medium", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50, self.level_medium)
            hard_button = Button("Hard", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 25, 200, 50, self.level_hard)
            come_back_button = Button("Come Back", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 75, 200, 50, self.show_main_menu)

            menu.add_button(easy_button)
            menu.add_button(medium_button)
            menu.add_button(hard_button)
            menu.add_button(come_back_button)
            
            self.level_buttons_shown = True    # Updates the control variable
        
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
        # self.run()
        
        for button in self.buttons:
            button.action_triggered = False

    def start_game(self):
        print("Starting the game...")
        
        if self.current_level:
            python_command = "python"
            script_path = "run.py"
            
            # Start the game in a new process
            subprocess.run([python_command, script_path])

            # Reset the menu state after the game ends
            # self.show_main_menu()
            
            # Reset the control variable
            self.level_buttons_shown = False

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
    menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create buttons and add them to the menu
    menu.create_main_menu_buttons()

    menu.run()

if __name__ == "__main__":
    main()
'''