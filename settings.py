import pygame

class Settings():
    '''class store all settings for Space invaders'''

    def __init__(self):
        '''Initialize the game's settings'''

        #Field
        self.screen_wigth = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.screen_image = pygame.image.load('/home/damir/projects/python/space_invaders/pic/space.png')
        
        #Ship
        self.ship_limit = 3

        #Bullet
        self.bullet_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_height = 15

        self.bullet_color = 200, 200, 0

        #Alien
        self.fleet_drop_speed = 15

        #how quickly the alien point values increase
        self.score_scale = 1.5
        #how quickly the game speeds up
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game'''
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.3
        self.alien_points = 50

        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        

    def increase_speed(self):
        '''increase speed settings'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
