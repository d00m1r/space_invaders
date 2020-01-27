import sys
import pygame

from game_const import *

def run():
    pygame.init()
    screen = pygame.display.set_mode((WINSIZE, WINSIZE))
    pygame.display.set_caption('Space invaders')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill(BG_COL)
        pygame.display.flip()
        #clock.tick(30)
    #pygame.quit()

if __name__ == '__main__':
    run()