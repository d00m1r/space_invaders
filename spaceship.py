import pygame

class Ship():

    def __init__(self, screen):
        '''Initialize the ship'''

        self.screen = screen

        #convert() speeds up surface rendering
        self.image = pygame.image.load('/home/damir/projects/python/space_invaders/pic/player.png').convert()

        #make the background of the picture transparent
        self.image.set_colorkey((0, 0, 0))
        #all elements in game is rects
        self.ship_rect = self.image.get_rect(bottomright=(50, 50))
        self.screen_rect = screen.get_rect()

        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

    def draw_ship(self):
        self.screen.blit(self.image, self.ship_rect)