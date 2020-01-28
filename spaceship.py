import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''Initialize the ship'''

        self.screen = screen
        self.ai_settings = ai_settings

        #convert() speeds up surface rendering
        self.image = pygame.image.load('/home/damir/projects/python/space_invaders/pic/spaceship.png').convert()

        #make the background of the picture transparent
        self.image.set_colorkey((0, 0, 0))

        #all elements in game is rects
        self.ship_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.ship_rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def draw_ship(self):
        self.update()
        self.screen.blit(self.image, self.ship_rect)

    def update(self):
        """Update the ship's position based on the movement flags"""

        # Update the ship's center value, not the rect
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.ship_rect.centerx = self.center