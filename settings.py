class Settings():
    '''class store all settings for Space invaders'''

    def __init__(self):
        '''Initialize the game's settings'''

        #Field
        self.screen_wigth = 800
        self.screen_height = 800
        self.bg_color = (100, 100, 100)

        #Ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet
        self.bullet_speed_factor = 7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 0
        self.bullets_allowed = 100

        #Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

