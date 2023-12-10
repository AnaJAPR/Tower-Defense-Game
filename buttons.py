import pygame

class Button():
    """
    Represent the buttons used in game, such as exit and add turrets.

    Parameters
    ---------- 
    x : int
        x coordinate of the top-left corner of the button.
    y : int
        y coordinate of the top-left corner of the button.
    image_path : str
        A string containing the path to the image of the button.
    
    Attributes
    ----------
    x : int
        x coordinate of the top-left corner of the button.
    y : int
        y coordinate of the top-left corner of the button.
    image : pygame.surface.Surface
        An image of the button loaded using pygame.
    rect : pygame.rect.Rect
        Rect where the image is drawn.
    rect.topleft : tuple 
        Coordinates x and y for the topleft of the rect.
    clicked : bool
        Represents whether the button is currently being clicked (True) or not (False).

    Example
    -------
    button = Button(500, 500, "assets/buttons/exit.png")
    """
    def __init__(self, x:int, y:int, image_path:str):
        """
        Initialize a new instance of the Button class

        Parameters
        ---------- 
        x : int
            x coordinate of the top-left corner of the button.
        y : int
            y coordinate of the top-left corner of the button.
        image_path : str
            A string containing the path to the image of the button.
        """
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def transform_image_proportions(self, width:int, height:int):
        """
        Transform the image proportions to a specified width and height using Pygame's
        transform.scale function.

        Parameters
        ---------- 
        width: int
            The desired width of the image.
        height: int
            The desired height of the image.

        Example
        -------
        button = Button(500, 500, "assets/buttons/exit.png")
        button.transform_image_proportions(69, 42)
        """
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw_button(self, surface:pygame.surface.Surface):
        """
        Draw the button on the specified surface and implement the act of clicking
        it.

        Parameters
        ---------- 
        surface : pygame.surface.Surface
            The surface on which the button will be drawn.
        
        Returns
        -------
        bool
            Return True if the button is being clicked, False otherwise.

        Example
        -------
        button = Button(500, 500, "assets/buttons/exit.png")
        button.draw_button(screen)
        """
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
    """
    Represent the buttons used in game, such as pause and add turrets.

    Parameters
    ---------- 
    x : int
        x coordinate of the top-left corner of the button.
    y : int
        y coordinate of the top-left corner of the button.
    image_path : str
        A string containing the path to the first stage image of the button.
    second_image_path : str
        A string containing the path to the second stage image of the button.
    
    Attributes
    ----------
    x : int
        x coordinate of the top-left corner of the button.
    y : int
        y coordinate of the top-left corner of the button.
    image : pygame.surface.Surface
        An image of the first stage of the button loaded using pygame.
    rect : pygame.rect.Rect
        Rect where the image is drawn.
    rect.topleft : tuple 
        Coordinates x and y for the topleft of the rect.
    second_image : pygame.surface.Surface
        An image of the second stage of the button loaded using pygame.
    second_rect : pygame.rect.Rect
        Rect where the second image is drawn.
    second_rect.topleft : tuple
        Coordinates x and y for the topleft of the second image rect.
    clicked : bool
        Represents whether the button is currently being clicked (True) or not (False).
    status : bool
        Represents using True or False if the button is on the first or second stage.

    Example
    -------
    two_action_button = TwoActionButton(500, 500, "assets/buttons/continue.png", "assets/buttons/pause.png")
    """
    def __init__(self, x:int, y:int, image_path:str, second_image_path:str):
        """
        Initialize a new instance of the TwoActionButton class

        Parameters
        ---------- 
        x : int
            x coordinate of the top-left corner of the button.
        y : int
            y coordinate of the top-left corner of the button.
        image_path : str
            A string containing the path to the first stage image of the button.
        second_image_path : str
            A string containing the path to the second stage image of the button.
        """
        super().__init__(x, y, image_path)
        self.second_image = pygame.image.load(second_image_path).convert_alpha()
        self.second_rect = self.second_image.get_rect()
        self.second_rect.topleft = (x, y)
        self.status = True

    def transform_image_proportions(self, width: int, height: int):
        """
        Transform the images proportions to a specified width and height using Pygame's
        transform.scale function.

        Parameters
        ---------- 
        width: int
            The desired width of the image.
        height: int
            The desired height of the image.

        Example
        -------
        two_action_button = TwoActionButton(500, 500, "assets/buttons/continue.png", "assets/buttons/pause.png")
        two_action_button.transform_image_proportions(69, 42)
        """    
        self.second_image = pygame.transform.scale(self.second_image, (width, height))
        self.second_rect = self.second_image.get_rect()
        self.second_rect.topleft = (self.x, self.y)
        super().transform_image_proportions(width, height)
         
    def draw_button(self, surface):
        """
        Draw the button on the specified surface and implement the act of clicking
        it and changing its appearance.

        Parameters
        ---------- 
        surface : pygame.surface.Surface
            The surface on which the button will be drawn.
        
        Returns
        -------
        bool
            Return True if the button is being clicked, False otherwise.

        Example
        -------
        two_action_button = TwoActionButton(500, 500, "assets/buttons/continue.png", "assets/buttons/pause.png")
        two_action_button.draw_button(screen)
        """
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
            surface.blit(self.second_image, self.second_rect)
    
        return action