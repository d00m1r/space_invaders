import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from spaceship import Ship
from alien import Alien


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption('Space invaders')

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)

    #make a group to store bullets in
    bullets = Group()
    aliens = Group()

    #create he fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, ship)
    
    #main loop
    while True:
        gf.check_events(ai_settings, ship, screen, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


if __name__ == '__main__':
    run()