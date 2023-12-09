import pygame
import sys
import subprocess
import os

class Button:
    def __init__(self, image, pos, text_input, base_color, hovering_color, min_size=(100, 50)):
        # Initialize a Button object with its position, size, text, and associated action
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
        pygame.mixer.init()
        pygame.mixer.music.load("assets/menu_audios_images/menu_audio.mp3")
        pygame.mixer.music.set_volume(0.5)    # sets the volume
        pygame.mixer.music.play(-1)    # Plays the song in an infinite loop (-1)
        self.SOUND_TOGGLE = Button(
            image=pygame.transform.scale(pygame.image.load("assets/buttons/sound.jpg"), (40, 40)),
            pos=(760, 25), text_input="", base_color="White", hovering_color="Green")
        self.sound_enabled = True   # Indicates whether the sound is enabled or not
        
        bg_image = pygame.image.load("assets/menu_audios_images/menu_background.jpeg")
        self.BG = pygame.transform.scale(bg_image, (800, 600))
        self.SCREEN = pygame.display.set_mode(self.BG.get_rect().size)
        pygame.display.set_caption("Tower Defense Menu")
        self.play_button = Button(image=pygame.image.load("assets/buttons/play_rect.png"), pos=(640,250),
                                  text_input="PLAY", base_color="LightGreen", hovering_color="White")
        self.start_game_button = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 + 50),
                                  text_input="START GAME", base_color="White", hovering_color="Green")
        self.game_running = False
        self.run()
    
    def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill((0,0,0))

            PLAY_TEXT = pygame.font.Font(None, 36).render("Starting the game...", True, (255, 255, 255))
            PLAY_RECT = PLAY_TEXT.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT)
            
            self.start_game_button.changeColor(PLAY_MOUSE_POS)
            self.start_game_button.update(self.SCREEN)

            PLAY_BACK = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() - 40), 
                            text_input="BACK", base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button.checkForInput(PLAY_MOUSE_POS) and not self.game_running:
                        self.start_game()
                    elif PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()
                        
            pygame.display.update()

    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill((255,255,255))

            OPTIONS_TEXT = pygame.font.Font(None, 36).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() - 40), 
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

    def start_game(self):
        print("Starting the game...")

        python_command = "python"
        script_path = "run.py"
            
        # Start the game in a new process
        subprocess.Popen([python_command, script_path])
        sys.exit()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            PLAY_BUTTON = Button(image=pygame.image.load("assets/buttons/play_rect.png"), pos=(640, 250), 
                            text_input="PLAY", base_color="LightGreen", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/buttons/options_rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", base_color="LightGreen", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/buttons/quit_rect.png"), pos=(640, 550), 
                            text_input="QUIT", base_color="LightGreen", hovering_color="White")

            for button in [self.play_button, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    elif self.SOUND_TOGGLE.checkForInput(MENU_MOUSE_POS):
                        self.toggle_sound()

            self.SOUND_TOGGLE.changeColor(MENU_MOUSE_POS)
            self.SOUND_TOGGLE.update(self.SCREEN)
            pygame.display.update()
            
    def toggle_sound(self):
        if self.sound_enabled:
            pygame.mixer.music.pause()
            self.SOUND_TOGGLE.image = pygame.transform.scale(pygame.image.load("assets/buttons/sound_off.jpg"), (40,40))
        else:
            pygame.mixer.music.unpause()
            self.SOUND_TOGGLE.image = pygame.transform.scale(pygame.image.load("assets/buttons/sound.jpg"), (40,40))
        self.sound_enabled = not self.sound_enabled
            
    def run(self):
        self.main_menu()

if __name__ == "__main__":
    menu = Menu()