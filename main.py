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
from scoreboard import Scoreboard


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption('Space invaders')

    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #main loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens)
        if stats.game_active:
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_bullets(aliens, bullets, ai_settings, screen, stats, sb, ship)
        gf.update_screen(ai_settings, stats, screen, sb, ship, bullets, aliens, play_button)


if __name__ == '__main__':
    run()