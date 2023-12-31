import pygame
import sys
import subprocess

class Button:
    """
    Represents an interactive button in a graphical interface.

    Parameters
    ----------
    image : pygame.surface.Surface
        The image associated with the button. Can be None if the button has no image.
    pos : tuple
        The initial position of the button as a tuple (x, y).
    text_input : str
        The text to be displayed on the button.
    base_color : tuple or str
        The base color of the button when not hovered, specified as an RGB tuple or as a string with the name of a color.
    hovering_color : tuple
        The base color of the button when hovered over, specified as an RGB tuple or as a string with the name of a color.
    min_size : tuple, optional
        Minimum size of the button, specified as (width, height). Default is (100, 50).

    Attributes
    ----------
    image : pygame.surface.Surface
        An image of the button loaded using pygame.
    x_pos : int
        x coordinate of the top-left corner of the button.
    y_pos : int
        y coordinate of the top-left corner of the button.
    base_color : tuple or str
        The base color of the button when not hovered, specified as an RGB tuple or as a string with the name of a color.
    hovering_color : tuple or str
        The base color of the button when hovered over, specified as an RGB tuple or as a string with the name of a color.
    text_input : str
        The text to be displayed on the button.
    font_size : int
        Font size for the button text.
    font : pygame.font.Font
        Font object for rendering text.
    text : pygame.surface.Surface
        Rendered text surface.
    rect : pygame.rect.Rect
        Rectangular area where the button is drawn.

    Example
    -------
    START_GAME_BUTTON = Button(image=None, pos=(560,25), text_input="START GAME", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
    """
    
    def __init__(self, image, pos:tuple, text_input, base_color, hovering_color, min_size=(100, 50)):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.font_size = 36
        self.font = pygame.font.SysFont(None, self.font_size)
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """
        Updates the representation of the button on the screen.

        Parameters
        ----------
        screen : pygame.surface.Surface
            The Pygame screen where the button will be rendered.

        Example
        -------
        START_GAME_BUTTON = Button(image=None, pos=(560,25), text_input="START GAME", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
        START_GAME_BUTTON.update(pygame.display.get_surface())
        """
        
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.rect)
        
    def checkForInput(self, position):
        """
        Checks if the given position is over the button.

        Parameters
        ----------
        position : tuple
            The position to be checked as a tuple (x, y).

        Returns
        -------
        bool
            True if the position is over the button, False otherwise.

        Example
        -------
        START_GAME_BUTTON = Button(image=None, pos=(560,25), text_input="START GAME", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
        is_over = START_GAME_BUTTON.checkForInput((520, 520))
        """
        
        return self.rect.collidepoint(position)
    
    def changeColor(self, position):
        """
        Changes the color of the button based on the mouse position.

        Parameters
        ----------
        position : tuple
            The mouse position as a tuple (x, y).
        
        Returns
        -------
        None

        Example
        -------
        START_GAME_BUTTON = Button(image=None, pos=(560,25), text_input="START GAME", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
        START_GAME_BUTTON.changeColor((520, 520))
        """
        
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

# function to place texts with line breaks on the rendered screen
def draw_multiline_text(screen, font, text_lines, text_col, x, y, line_height):
    for i, line in enumerate(text_lines):
        img = font.render(line, True, text_col)
        screen.blit(img, (x, y + i * line_height))
        

class Menu:
    """
    Represents a graphical interface for the game menu.

    This class initializes the game menu, defines its buttons, and specifies actions associated with them.

    Attributes
    ----------
    SOUND_TOGGLE : Button
        Button for toggling sound.
    sound_enabled : bool
        Indicates whether the sound is enabled or not.
    BG : pygame.surface.Surface
        Background image of the menu.
    SCREEN : pygame.surface.Surface
        Pygame screen for displaying the menu.
    game_running : bool
        Represents whether the game is currently running (True) or not (False).

    Example
    -------
    menu = Menu()
    menu.run()
    """
    
    def __init__(self):
        """
        Initialize the Menu.

        Example
        -------
        menu = Menu()
        """
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/menu_audios_images/menu_audio.mp3")
        pygame.mixer.music.set_volume(1)    # sets the volume
        pygame.mixer.music.play(-1)    # Plays the song in an infinite loop (-1)
        self.SOUND_TOGGLE = Button(
            image=pygame.transform.scale(pygame.image.load("assets/buttons/sound.png"), (40, 40)),
            pos=(760, 25), text_input="", base_color="White", hovering_color="Green")
        self.sound_enabled = True   # Indicates whether the sound is enabled or not
        
        bg_image = pygame.image.load("assets/menu_audios_images/menu_background.jpeg")
        self.BG = pygame.transform.scale(bg_image, (800, 600))
        self.SCREEN = pygame.display.set_mode(self.BG.get_rect().size)
        pygame.display.set_caption("Tower Defense Menu")
        self.game_running = False
        self.run()
    
    def play(self):
        """
        Display the screen for starting the game.

        Example
        -------
        menu.play()
        """
        
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            # Setting the screen background
            self.SCREEN.fill((254,217,139))
            
            start_game_text_lines = [
            "The year is 1999, and the world has fallen in chaos after World War Three.",
            "Cities have fallen, countries have been nuked,",
            "and few bastions of humanity remain. You, an engineer,",
            "are tasked to defend one of the last holds of your motherland",
            "from the air raids of your enemies, and for that, you have your turrets.", 
            "Build them in strategic points, push back the attack, protect your home!",
            "Do you have what it takes to protect the last front against decimation?"
            ]
            
            x = self.SCREEN.get_width() // 15
            y = self.SCREEN.get_height() // 3

            # Calculates the total height of rendered text
            line_height = 30
            total_height = len(start_game_text_lines) * line_height

            # Adjusts the starting position (y) to center the text vertically
            y -= total_height // 2

            draw_multiline_text(self.SCREEN, pygame.font.Font(None, 30), start_game_text_lines, (94, 88, 49), x, y, line_height)
            
            # defining a button using the Button class
            START_GAME_BUTTON = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 + 50),
                                  text_input="START GAME", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
            
            START_GAME_BUTTON.changeColor(PLAY_MOUSE_POS)
            START_GAME_BUTTON.update(self.SCREEN)

            # defining a button using the Button class
            PLAY_BACK = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() - 40), 
                            text_input="BACK", base_color=(94, 88, 49), hovering_color=(207, 126, 18))

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                # if close the window exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # If you click on start and then on start game the game starts, if you click on back it runs the initial menu again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_GAME_BUTTON.checkForInput(PLAY_MOUSE_POS) and not self.game_running:
                        self.start_game()
                    elif PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()
                        
            pygame.display.update()

    def sobre_o_jogo(self):
        """
        Display the screen for information about the game.

        Example
        -------
        menu.sobre_o_jogo()
        """

        while True:
            ABOUT_THE_GAME_MOUSE_POS = pygame.mouse.get_pos()

            # Setting the screen background
            self.SCREEN.fill((254,217,139))

            about_the_game_text_lines = [
            "How to play?",
            "",
            "When you click on 'start game' the game starts, with pause activated.",
            "There are buttons at the bottom of the game screen, two of which",
            "you must click to buy an artillery or laser turret",
            "and select the base of the map where it will be located."
            "After positioning the towers in the desired locations, you must start",
            "the game by activating the unpause button in the upper right corner.",
            "Enemies begin to pass through the map and towers shoot causing",
            "damage. If you let enemies reach the end of the route, your life,",
            "which is in the upper left corner along with your money, reduces.",
            "Whenever an enemy loses all health, you gain more money.",
            "You can add and remove towers during the game. If you run out",
            "of life before the enemies run out, you lose. Otherwise your",
            "game gets stars from 1 to 3, so 1 means you won, 2 means you won",
            "with at least half your life and 3 that you won without losing life",
            ]

            x = self.SCREEN.get_width() // 35
            y = self.SCREEN.get_height() // 2

            # Calculates the total height of rendered text
            line_height = 30
            total_height = len(about_the_game_text_lines) * line_height

            # Adjust starting position (y) to center text vertically
            y -= total_height // 2

            draw_multiline_text(self.SCREEN, pygame.font.Font(None, 28), about_the_game_text_lines, (94, 88, 49), x, y, line_height)

            ABOUT_THE_GAME_BACK = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() - 40), 
                            text_input="BACK", base_color=(94, 88, 49), hovering_color=(207, 126, 18))

            ABOUT_THE_GAME_BACK.changeColor(ABOUT_THE_GAME_MOUSE_POS)
            ABOUT_THE_GAME_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ABOUT_THE_GAME_BACK.checkForInput(ABOUT_THE_GAME_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()
            
    def confirm_quit(self):
        """
        Display the screen to confirm quitting the game.

        Example
        -------
        menu.confirm_quit()
        """
        
        while True:
            # Setting the screen background
            self.SCREEN.fill((254,217,139))

            CONFIRM_TEXT = pygame.font.Font(None, 36).render("Você tem certeza que deseja sair?", True, (94, 88, 49))
            CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 - 50))
            self.SCREEN.blit(CONFIRM_TEXT, CONFIRM_RECT)

            # defining buttons using the Button class
            YES_BUTTON = Button(image=None, pos=(self.SCREEN.get_width() // 2 - 100, self.SCREEN.get_height() // 2 + 50),
                                text_input="SIM", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
            NO_BUTTON = Button(image=None, pos=(self.SCREEN.get_width() // 2 + 100, self.SCREEN.get_height() // 2 + 50),
                               text_input="NÃO", base_color=(94, 88, 49), hovering_color=(207, 126, 18))

            # buttons change color when you position the mouse over them
            YES_BUTTON.changeColor(pygame.mouse.get_pos())
            YES_BUTTON.update(self.SCREEN)

            NO_BUTTON.changeColor(pygame.mouse.get_pos())
            NO_BUTTON.update(self.SCREEN)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if YES_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    elif NO_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        return

    def start_game(self):
        """
        Start the game in a new process.

        Example
        -------
        menu.start_game()
        """

        print("Starting the game...")

        python_command = "python"
        script_path = "run.py"
            
        # Start the game in a new process
        subprocess.Popen([python_command, script_path])
        sys.exit()

    def main_menu(self):
        """
        Display the main menu.

        Example
        -------
        menu.main_menu()
        """        

        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # defining buttons using the Button class
            PLAY_BUTTON = Button(image=pygame.image.load("assets/buttons/play_rect.png"), pos=(640,250),
                                text_input="PLAY", base_color=(254,217,139), hovering_color="White")
            ABOUT_THE_GAME_BUTTON = Button(image=pygame.image.load("assets/buttons/about_the_game_rect.png"), pos=(640, 400), 
                                text_input="ABOUT THE GAME", base_color=(254,217,139), hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/buttons/quit_rect.png"), pos=(640, 550), 
                                text_input="QUIT", base_color=(254,217,139), hovering_color="White")

            # buttons change color when you position the mouse over them
            for button in [PLAY_BUTTON, ABOUT_THE_GAME_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            # handles events relating to each home menu button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    elif ABOUT_THE_GAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sobre_o_jogo()
                    elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.confirm_quit()
                    elif self.SOUND_TOGGLE.checkForInput(MENU_MOUSE_POS):
                        self.toggle_sound()

            # button changes color when you position the mouse over them
            self.SOUND_TOGGLE.changeColor(MENU_MOUSE_POS)
            self.SOUND_TOGGLE.update(self.SCREEN)
            pygame.display.update()
            
    def toggle_sound(self):
        """
        Toggle the sound between on and off.

        Example
        -------
        menu.toggle_sound()
        """
        
        if self.sound_enabled:
            pygame.mixer.music.pause()
            self.SOUND_TOGGLE.image = pygame.transform.scale(pygame.image.load("assets/buttons/sound_off.png"), (40,40))
        else:
            pygame.mixer.music.unpause()
            self.SOUND_TOGGLE.image = pygame.transform.scale(pygame.image.load("assets/buttons/sound.png"), (40,40))
        self.sound_enabled = not self.sound_enabled
            
    def run(self):
        """
        Run the main menu.

        Example
        -------
        menu.run()
        """

        self.main_menu()

