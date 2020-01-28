import sys
import pygame


def check_events(ai_settings, ship):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            #spaceship moving
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

                
def update_screen(ai_settings, screen, ship):
    '''Draw screen and elements'''
    ship.update()
    screen.fill(ai_settings.bg_color)
    ship.draw_ship()
    pygame.display.flip()
    #clock.tick(30)