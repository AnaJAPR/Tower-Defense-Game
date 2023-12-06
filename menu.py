import pygame
import sys

class Button:
    def __init__(self, text, x, y, width, height, action=None):
        # Initialize a Button object with its position, size, text, and associated action
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (186, 147, 216)
        self.hover_color = (160, 110, 200)
        self.text = text
        self.action = action

    def draw(self, screen):
        # Draw the button on the screen, change color when hovered, and execute action on click
        pygame.draw.rect(screen, self.color, self.rect)
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
            if mouse_click[0] == 1 and self.action is not None:
                self.action()

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Menu:
    def __init__(self, screen):
        # Initialize the menu with its associated screen and an empty list of buttons
        self.screen = screen
        self.buttons = []

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
                    return

            if event.type == pygame.VIDEORESIZE:
                self.handle_resize(event)

            for button in self.buttons:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button.rect.collidepoint(event.pos):
                    if button.text == "Start":
                        self.show_level_buttons() 
                    else:
                        button.action()

    def handle_resize(self, event):
        # Resize the screen and update button positions to remain centered
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        for i, button in enumerate(self.buttons):
            button.rect.x = SCREEN_WIDTH // 2 - button.rect.width // 2
            button.rect.y = SCREEN_HEIGHT // 2 - len(self.buttons) * 25 + i * 50

    # Main loop for handling events and updating the screen
    def run(self):
        while True:
            self.handle_events()
            self.screen.fill((255, 255, 255))
        
            for button in self.buttons:
                button.draw(self.screen)

            pygame.display.flip()
    
    def show_level_buttons(self):
        Menu.buttons.clear()

        easy_button = Button("Easy", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 75, 200, 50, start_game)
        middle_button = Button("Middle", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50, start_game)
        hard_button = Button("Hard", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 25, 200, 50, start_game)

        menu.add_button(easy_button)
        menu.add_button(middle_button)
        menu.add_button(hard_button)

def start_game():
    print("Starting the game...")

def toggle_sound():
    print("Toggling sound...")

def show_options():
    print("Showing options...")
    
def show_almanac():
    print("Showing almanac...")
    
def game_story():
    print("Telling the story of the game...")
    
def show_help():
    print("displaying help...")
    
def level_easy():
    print("Selected Easy level...")

def level_middle():
    print("Selected Middle level...")

def level_hard():
    print("Selected Hard level...")

def main():
    pygame.init()

    # Screen settings
    global SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Tower Defense Menu")

    menu = Menu(screen)

    # Create buttons and add them to the menu
    start_button = Button("Start", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50, start_game)
    options_button = Button("Options", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 25, 200, 50, show_options)
    almanac_button = Button("Almanac", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 75, 200, 50, show_almanac)
    game_story_button = Button("Game's story", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 125, 200, 50, game_story)
    help_button = Button("Help", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 175, 200, 50, show_help)

    menu.add_button(start_button)
    menu.add_button(options_button)
    menu.add_button(almanac_button)
    menu.add_button(game_story_button)
    menu.add_button(help_button)

    menu.run()

if __name__ == "__main__":
    main()
