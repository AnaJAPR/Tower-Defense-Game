import pygame

class Button():
    def __init__(self, x:int, y:int, image_path:str):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def transform_image_proportions(self, width:int, height:int):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

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
    
class TwoActionButton(Button):
    def __init__(self, x, y, image_path, image_path_dif):
        super().__init__(x, y, image_path)
        self.image_2 = pygame.image.load(image_path_dif).convert_alpha()
        self.rect_dif = self.image_2.get_rect()
        self.rect_dif.topleft = (x, y)
        self.status = True

    def transform_image_proportions(self, width: int, height: int):
        self.image_2 = pygame.transform.scale(self.image_2, (width, height))
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.topleft = (self.x, self.y)
        super().transform_image_proportions(width, height)
         
    def draw_button(self, surface):
        action = False
        position = pygame.mouse.get_pos()

        # Checking whether or not the button is being pressed
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                self.status = not self.status

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Drawing the button on the screen
        if self.status == True:
            surface.blit(self.image, self.rect)
        if self.status == False:
            surface.blit(self.image_2, self.rect_2)
    
        return action