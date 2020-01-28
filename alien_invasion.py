import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from spaceship import Ship


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption('Space invaders')
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets in.
    bullets = Group()
    
    #main loop
    while True:
        gf.check_events(ai_settings, ship, screen, bullets)

        #calls bullet.update() for each bullet we place in the group bullets
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.bul_rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)
    #pygame.quit()

if __name__ == '__main__':
    run()