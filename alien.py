import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''class to represent a single alien in the fleet'''
    def __init__(self, ai_settings, screen):

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('/home/damir/projects/python/space_invaders/pic/alien.png').convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255 ))

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
    
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        '''move the alien right or left'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''return True if alien is at adge of screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True