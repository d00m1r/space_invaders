"""run space invaders game"""
import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from spaceship import Ship
from alien import Alien
from button import Button


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption('Space invaders')

    #make the Play button
    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game statistics
    stats = GameStats(ai_settings)
    
    ship = Ship(ai_settings, screen)
    #alien = Alien(ai_settings, screen)

    #make a group to store bullets in
    bullets = Group()
    aliens = Group()

    #create he fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #main loop
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens)
        if stats.game_active:
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button)


if __name__ == '__main__':
    run()