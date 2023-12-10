import pygame
import sys
import subprocess

class Button:
    def __init__(self, image, pos, text_input, base_color, hovering_color, min_size=(100, 50)):
        '''
        
        
        '''
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
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill((254,217,139))

            PLAY_TEXT = pygame.font.Font(None, 36).render("Starting the game...", True, (94, 88, 49))
            PLAY_RECT = PLAY_TEXT.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT)
            
            START_GAME_BUTTON = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 + 50),
                                  text_input="START GAME", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
            
            START_GAME_BUTTON.changeColor(PLAY_MOUSE_POS)
            START_GAME_BUTTON.update(self.SCREEN)

            PLAY_BACK = Button(image=None, pos=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() - 40), 
                            text_input="BACK", base_color=(94, 88, 49), hovering_color=(207, 126, 18))

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_GAME_BUTTON.checkForInput(PLAY_MOUSE_POS) and not self.game_running:
                        self.start_game()
                    elif PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()
                        
            pygame.display.update()

    def sobre_o_jogo(self):
        while True:
            ABOUT_THE_GAME_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill((254,217,139))

            ABOUT_THE_GAME_TEXT = pygame.font.Font(None, 36).render("This is the ABOUT THE GAME screen.", True, (94, 88, 49))
            ABOUT_THE_GAME_RECT = ABOUT_THE_GAME_TEXT.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2))
            self.SCREEN.blit(ABOUT_THE_GAME_TEXT, ABOUT_THE_GAME_RECT)

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
        while True:
            self.SCREEN.fill((254,217,139))

            CONFIRM_TEXT = pygame.font.Font(None, 36).render("Você tem certeza que deseja sair?", True, (94, 88, 49))
            CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 - 50))
            self.SCREEN.blit(CONFIRM_TEXT, CONFIRM_RECT)

            YES_BUTTON = Button(image=None, pos=(self.SCREEN.get_width() // 2 - 100, self.SCREEN.get_height() // 2 + 50),
                                text_input="SIM", base_color=(94, 88, 49), hovering_color=(207, 126, 18))
            NO_BUTTON = Button(image=None, pos=(self.SCREEN.get_width() // 2 + 100, self.SCREEN.get_height() // 2 + 50),
                               text_input="NÃO", base_color=(94, 88, 49), hovering_color=(207, 126, 18))

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

            PLAY_BUTTON = Button(image=pygame.image.load("assets/buttons/play_rect.png"), pos=(640,250),
                                text_input="PLAY", base_color=(254,217,139), hovering_color="White")
            ABOUT_THE_GAME_BUTTON = Button(image=pygame.image.load("assets/buttons/about_the_game_rect.png"), pos=(640, 400), 
                                text_input="ABOUT THE GAME", base_color=(254,217,139), hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/buttons/quit_rect.png"), pos=(640, 550), 
                                text_input="QUIT", base_color=(254,217,139), hovering_color="White")

            for button in [PLAY_BUTTON, ABOUT_THE_GAME_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
        
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

            self.SOUND_TOGGLE.changeColor(MENU_MOUSE_POS)
            self.SOUND_TOGGLE.update(self.SCREEN)
            pygame.display.update()
            
    def toggle_sound(self):
        if self.sound_enabled:
            pygame.mixer.music.pause()
            self.SOUND_TOGGLE.image = pygame.transform.scale(pygame.image.load("assets/buttons/sound_off.png"), (40,40))
        else:
            pygame.mixer.music.unpause()
            self.SOUND_TOGGLE.image = pygame.transform.scale(pygame.image.load("assets/buttons/sound.png"), (40,40))
        self.sound_enabled = not self.sound_enabled
            
    def run(self):
        self.main_menu()

if __name__ == "__main__":
    menu = Menu()