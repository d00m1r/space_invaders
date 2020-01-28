import sys
import pygame


def check_events():
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(ai_settings, screen, ship):
    '''Draw screen and elements'''
    screen.fill(ai_settings.bg_color)
    ship.draw_ship()
    pygame.display.flip()
    #clock.tick(30)