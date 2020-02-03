import pygame.font
from pygame.sprite import Group
from spaceship import Ship

class Scoreboard():
    '''report scroting information'''
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #font settings for scoring information
        self.text_color = (0, 200, 0)
        self.font = pygame.font.SysFont(None, 48)
        
        #prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_ships()

    def prep_score(self):
        '''turn the score into a rendered image'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        
        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 15
        self.score_rect.top = 15

    def prep_high_score(self):
        '''turn the high score into a rendered image'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.ai_settings.bg_color)

        #center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_lvl(self):
        '''turn the level into a rendered image'''
        self.lvl_image = self.font.render('lvl ' + str(self.stats.lvl), True, self.text_color, self.ai_settings.bg_color)
        #position the level below the score
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        '''show how many ships are left'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''draw score to the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)