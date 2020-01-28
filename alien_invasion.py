import sys
import pygame

#from game_const import *
import game_functions as gf
from settings import Settings
from spaceship import Ship


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption('Space invaders')
    
    ship = Ship(screen)

    #main loop
    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
    #pygame.quit()

if __name__ == '__main__':
    run()