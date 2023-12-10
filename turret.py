import pygame
import constants as c
from game import load_levels as ll
from game import load_enemy as le
from turret_data import TURRET_DATA
import math

class BaseTurret(pygame.sprite.Sprite):
    """
    Represents the turret and its mechanics.

    Parameters
    ---------- 
    sprite_sheets :  list
        A list containing the turret images.
    pos_x : int
        The x coordinate of the closest base.
    pos_y : int
        The y coordinate of the closest base.
    price : int
        The turret price.
    sfx : pygame.mixer.Sound
        Sound effects of the turret.
    turret_type : str
        The turret type.
    
    Attributes
    ----------
    upgrade level : int
        Current level of the turret.
    turret_type : str
        The turret type.
    range : int
        Range where the turret can hit an enemy.
    cooldown : int
        Time in milliseconds between one shot and another.
    damage : float
        Damage a tower can deal.
    last_shot : int
        When the last shot happened.
    selected : bool
        If the tower is selected or not.
    target : enemy.Enemy
        The enemy that the turret is currently targeting.
    price : int
        The turret price.
    upgrade_price : int
        The price the player must pay to upgrade the turret
    pos_x : int
        The x coordinate of the turret.
    pos_y : int
        The y coordinate of the turret.
    sfx : pygame.mixer.Sound
        Sound effects of the turret.
    sprite_sheets :  list
        A list containing turret images.
    animation_list : list
        A list containing the images in order to animate them.
    frame_index : int
        Index of the frame of the animation.
    update_time : int
        Time used to update the tower animations.
    angle : int
        Angle that the tower is turned.
    original_image : pygame.surface.Surface
        Image of the turret in its currently stage of the animation.
    image : pygame.surface.Surface
        Original image of the tower after being turned according to the angle.
    rect : pygame.rect.Rect
        Rectangle where the turret image is drawn.
    rect.center : tuple 
        Coordinates x and y for the center of the rectangle.
    range_image : pygame.surface.Surface
        Image of the range that the turret can hit an enemy.
    range_rect : pygame.rect.Rect
        Rectangle where the range image is drawn.
    range_rect.center : tuple
        Tuple containing the x and y coordinates of the center of the range rectangle.
    
    Example
    -------
    turret = Turret(image_list, 500, 500, 100, song, "artillery")
    """

    def __init__(self, sprite_sheets, pos_x, pos_y, price, sfx, turret_type):
        """
        Initialize a new instance of the BaseTurret class.

        Parameters
        ---------- 
        sprite_sheets :  list
            A list containing the turret images.
        pos_x : int
            The x coordinate of the closest base.
        pos_y : int
            The y coordinate of the closest base.
        price : int
            The turret price.
        sfx : pygame.mixer.Sound
            Sound effects of the turret.
        turret_type : str
            The turret type.
        """
        pygame.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.turret_type = turret_type

        self.range = TURRET_DATA[self.turret_type][self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.turret_type][self.upgrade_level - 1].get("cooldown")
        self.damage = TURRET_DATA[self.turret_type][self.upgrade_level - 1].get("damage")
        self.last_shot = pygame.time.get_ticks()
        self.selected = False
        self.target = None
        self.price = price
        self.upgrade_price = self.price + 10

        # Position variables
        self.pos_x = pos_x
        self.pos_y = pos_y

        # Sound effects
        self.sfx = sfx
        
        # Animation variables
        self.sprite_sheets = sprite_sheets
        self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        # Update image
        self.angle = 90
        self.original_image = self.animation_list[self.frame_index]
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

        # Create range radius
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def load_images(self, sprite_sheet):
        """
        Extract the images from the sprite sheet and create an animation list.

        Parameters
        ---------- 
        sprite_sheet : list
            A list containing the turret images
        
        Returns
        -------
        list
            A list containing the turret frames for the animation.

        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.load_image(sprite_sheet)
        """
        # Extracts images from spritesheet
        size = sprite_sheet.get_height()
        animation_list = []
        for x in range(c.ANIMATION_STEPS):
            temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_img)
        return animation_list
    
    def update(self, enemy_group):
        """
        Updates the animations of the turret, choosing its target and rotating it.

        Parameters
        ---------- 
        enemy_group : pygame.sprite.Group
            The group of enemies that the turret attacks.

        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.update(enemy_group)
        """
        # If target picked, play firing animation
        if self.target:
            self.play_animation()
        else:
            # Search for a new target once turret has cooled down
            if pygame.time.get_ticks() - self.last_shot > (self.cooldown / ll.level.game_speed):
                self.pick_target(le.enemy_group)
    
    def pick_target(self, enemy_group):
        """
        Causes the turret to choose its target.

        Parameters
        ---------- 
        enemy_group : pygame.sprite.Group
            The group of enemies that the turret attacks.

        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.pick_target(enemy_group)
        """
        # Find an enemy to target
        x_dist = 0
        y_dist = 0
        # Check the distance to each enemy to see if it is in range
        for enemy in le.enemy_group:
            x_dist = enemy.position[0] - self.pos_x
            y_dist = enemy.position[1] - self.pos_y
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
                self.target = enemy
                self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                # Deal damage to the enemy
                self.target.health -= self.damage
                # Play sound effect
                self.sfx.play()
                break

    def play_animation(self):
        """
        Plays the animation of the turret.

        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.play_animation()
        """

        # Update image
        self.original_image = self.animation_list[self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            # Check if the animation has finished and reset to idle
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
                # Record completed time and clear the target so cooldown restarts
                self.last_shot = pygame.time.get_ticks()
                self.target = None
    
    def upgrade(self):
        """
        Updates turret information.

        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.play_animation()
        """

        self.upgrade_level += 1
        if self.upgrade_level > 2:
            self.upgrade_price += self.upgrade_price // 2
        self.range = TURRET_DATA[self.turret_type][self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.turret_type][self.upgrade_level - 1].get("cooldown")
        self.damage = TURRET_DATA[self.turret_type][self.upgrade_level - 1].get("damage")
        # Upgrade turret image
        self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
        self.original_image = self.animation_list[self.frame_index]

        # Upgrade range radius
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self, surface):
        """
        Draws the turret on the specified surface.

        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.draw(screen)
        """
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

    def sell(self):
        """
        Sell the turret, making it disappear and earning the respective money.

        Returns
        -------
        bool
            Returns False to set variables to False while running.
            
        Example
        -------
            turret = Turret(image_list, 500, 500, 100, song, "artillery")
            turret.sell(screen)
        """
        removing = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                self.kill()
                ll.level.money += self.price + self.upgrade_price * (self.upgrade_level - 1)
        return removing

# Artillery Turret
class ArtilleryTurret(BaseTurret):
    """
    Represents the artillery turret and its mechanics.

    Parameters
    ---------- 
    sprite_sheets :  list
        A list containing the turret images.
    pos_x : int
        The x coordinate of the closest base.
    pos_y : int
        The y coordinate of the closest base.
    price : int
        The turret price.
    sfx : pygame.mixer.Sound
        Sound effects of the turret.
    turret_type : str
        The turret type, defined as "artillery".
    
    Attributes
    ----------
    upgrade level : int
        Current level of the turret.
    turret_type : str
        The turret type.
    range : int
        Range where the turret can hit an enemy.
    cooldown : int
        Time in milliseconds between one shot and another.
    damage : float
        Damage a tower can deal.
    last_shot : int
        When the last shot happened.
    selected : bool
        If the tower is selected or not.
    target : enemy.Enemy
        The enemy that the turret is currently targeting.
    price : int
        The turret price.
    upgrade_price : int
        The price the player must pay to upgrade the turret
    pos_x : int
        The x coordinate of the turret.
    pos_y : int
        The y coordinate of the turret.
    sfx : pygame.mixer.Sound
        Sound effects of the turret.
    sprite_sheets : list
        A list containing turret images.
    animation_list : list
        A list containing the images in order to animate them.
    frame_index : int
        Index of the frame of the animation.
    update_time : int
        Time used to update the tower animations.
    angle : int
        Angle that the tower is turned.
    original_image : pygame.surface.Surface
        Image of the turret in its currently stage of the animation.
    image : pygame.surface.Surface
        Original image of the tower after being turned according to the angle.
    rect : pygame.rect.Rect
        Rectangle where the turret image is drawn.
    rect.center : tuple 
        Coordinates x and y for the center of the rectangle.
    range_image : pygame.surface.Surface
        Image of the range that the turret can hit an enemy.
    range_rect : pygame.rect.Rect
        Rectangle where the range image is drawn.
    range_rect.center : tuple
        Tuple containing the x and y coordinates of the center of the range rectangle.
    
    Example
    -------
    turret = ArtilleryTurret(image_list, 500, 500, 100, song, "artillery")
    """
    def __init__(self, sprite_sheets, pos_x, pos_y, price, sfx):
        """
        Initialize a new instance of the Artillery Turret class.

        Parameters
        ---------- 
        sprite_sheets :  list
            A list containing the turret images.
        pos_x : int
            The x coordinate of the closest base.
        pos_y : int
            The y coordinate of the closest base.
        price : int
            The turret price.
        sfx : pygame.mixer.Sound
            Sound effects of the turret.
        turret_type : str
            The turret type, defined as "artillery".
        """
        super().__init__(sprite_sheets, pos_x, pos_y, price, sfx, turret_type="artillery")

# Laser Turret
class LaserTurret(BaseTurret):
    """
    Represents the laser turret and its mechanics.

    Parameters
    ---------- 
    sprite_sheets :  list
        A list containing the turret images.
    pos_x : int
        The x coordinate of the closest base.
    pos_y : int
        The y coordinate of the closest base.
    price : int
        The turret price.
    sfx : pygame.mixer.Sound
        Sound effects of the turret.
    turret_type : str
        The turret type, defined as "laser".
    
    Attributes
    ----------
    upgrade level : int
        Current level of the turret.
    turret_type : str
        The turret type.
    range : int
        Range where the turret can hit an enemy.
    cooldown : int
        Time in milliseconds between one shot and another.
    damage : float
        Damage a tower can deal.
    last_shot : int
        When the last shot happened.
    selected : bool
        If the tower is selected or not.
    target : enemy.Enemy
        The enemy that the turret is currently targeting.
    price : int
        The turret price.
    upgrade_price : int
        The price the player must pay to upgrade the turret
    pos_x : int
        The x coordinate of the turret.
    pos_y : int
        The y coordinate of the turret.
    sfx : pygame.mixer.Sound
        Sound effects of the turret.
    sprite_sheets :  list
        A list containing turret images.
    animation_list : list
        A list containing the images in order to animate them.
    frame_index : int
        Index of the frame of the animation.
    update_time : int
        Time used to update the tower animations.
    angle : int
        Angle that the tower is turned.
    original_image : pygame.surface.Surface
        Image of the turret in its currently stage of the animation.
    image : pygame.surface.Surface
        Original image of the tower after being turned according to the angle.
    rect : pygame.rect.Rect
        Rectangle where the turret image is drawn.
    rect.center : tuple 
        Coordinates x and y for the center of the rectangle.
    range_image : pygame.surface.Surface
        Image of the range that the turret can hit an enemy.
    range_rect : pygame.rect.Rect
        Rectangle where the range image is drawn.
    range_rect.center : tuple
        Tuple containing the x and y coordinates of the center of the range rectangle.
    
    Example
    -------
    turret = LaserTurret(image_list, 500, 500, 100, song, "laser")
    """
    def __init__(self, sprite_sheets, pos_x, pos_y, price, sfx):
        """
        Initialize a new instance of the Laser Turret class.

        Parameters
        ---------- 
        sprite_sheets :  list
            A list containing the turret images.
        pos_x : int
            The x coordinate of the closest base.
        pos_y : int
            The y coordinate of the closest base.
        price : int
            The turret price.
        sfx : pygame.mixer.Sound
            Sound effects of the turret.
        turret_type : str
            The turret type, defined as "laser".
        """
        super().__init__(sprite_sheets, pos_x, pos_y, price, sfx, turret_type="laser")
