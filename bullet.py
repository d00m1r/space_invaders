import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''class to manage bullets fired from the ship'''
    def __init__(self, ai_settings, screen, ship):
        '''create bullet obj at the ship's current position'''
        super().__init__()
        self.screen = screen

        #create a bullet rect at (0, 0) and then set correct position
        self.bul_rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.bul_rect.centerx = ship.ship_rect.centerx
        self.bul_rect.top = ship.ship_rect.top

        self.y = float(self.bul_rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor

        # Update the rect position.
        self.bul_rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.bul_rect)