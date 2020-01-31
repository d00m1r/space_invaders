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
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def draw_ship(self):
        self.update()
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flags"""

        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center