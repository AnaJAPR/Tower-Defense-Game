import pygame

class Button():
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def transform_image_proportions(self, width:int, height:int):
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw_button(self, surface):
        action = False
        position = pygame.mouse.get_pos()

        # Checking whether or not the button is being pressed
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Drawing the button on the screen
        surface.blit(self.image, self.rect)
        return action