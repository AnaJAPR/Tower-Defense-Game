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
    _x : int
        x coordinate of the top-left corner of the button.
    _y : int
        y coordinate of the top-left corner of the button.
    _image : pygame.surface.Surface
        An image of the button loaded using pygame.
    _rect : pygame.rect.Rect
        Rect where the image is drawn.
    _rect.topleft : tuple 
        Coordinates x and y for the topleft of the rect.
    _clicked : bool
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
        self._x = x
        self._y = y
        self._image = pygame.image.load(image_path).convert_alpha()
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._clicked = False

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
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._rect.topleft = (self._x, self._y)

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
        if self._rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self._clicked == False:
                action = True
                self._clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self._clicked = False

        # Drawing the button on the screen
        surface.blit(self._image, self._rect)
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
    _x : int
        x coordinate of the top-left corner of the button.
    _y : int
        y coordinate of the top-left corner of the button.
    _image : pygame.surface.Surface
        An image of the first stage of the button loaded using pygame.
    _rect : pygame.rect.Rect
        Rect where the image is drawn.
    _rect.topleft : tuple 
        Coordinates x and y for the topleft of the rect.
    _second_image : pygame.surface.Surface
        An image of the second stage of the button loaded using pygame.
    _second_rect : pygame.rect.Rect
        Rect where the second image is drawn.
    _second_rect.topleft : tuple
        Coordinates x and y for the topleft of the second image rect.
    _clicked : bool
        Represents whether the button is currently being clicked (True) or not (False).
    _status : bool
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
        self._second_image = pygame.image.load(second_image_path).convert_alpha()
        self._second_rect = self._second_image.get_rect()
        self._second_rect.topleft = (x, y)
        self.status = True

    def transform_image_proportions(self, width:int, height:int):
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
        self._second_image = pygame.transform.scale(self._second_image, (width, height))
        self._second_rect = self._second_image.get_rect()
        self._second_rect.topleft = (self._x, self._y)
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
        if self._rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self._clicked == False:
                action = True
                self._clicked = True
                self._status = not self._status

        if pygame.mouse.get_pressed()[0] == 0:
            self._clicked = False

        # Drawing the button on the screen
        if self._status == True:
            surface.blit(self._image, self._rect)
        if self._status == False:
            surface.blit(self._second_image, self._second_rect)
        return action

    @property
    def status(self):
        """
        Get the current status of the button.
        
        Returns
        -------
        bool
            Boolean that represents the current status of the button.
        
        Example
        -------
        two_action_button = TwoActionButton(500, 500, "assets/buttons/continue.png", "assets/buttons/pause.png")
        two_action_buttons.status
        """
        return self._status

    @status.setter
    def status(self, value:bool):
        """
        Set the status of the button to another value.

        Parameters
        ----------
        value : bool
            Update the button status according to a boolean.

        Example
        -------
        two_action_button = TwoActionButton(500, 500, "assets/buttons/continue.png", "assets/buttons/pause.png")
        two_action_buttons.status = False
        """
        self._status = value