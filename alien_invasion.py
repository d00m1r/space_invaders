import sys
import pygame

#from game_const import *
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Draw screen and elements
        screen.fill(ai_settings.bg_color)
        ship.draw_ship()
        pygame.display.flip()
        #clock.tick(30)
    #pygame.quit()

if __name__ == '__main__':
    run()