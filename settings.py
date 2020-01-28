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