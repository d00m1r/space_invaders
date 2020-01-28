import sys
import pygame

from bullet import Bullet


def check_events(ai_settings, ship, screen, bullets):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            #spaceship moving
            check_keypress_events(event, ship, screen, bullets, ai_settings)

def check_keypress_events(event, ship, screen, bullets, ai_settings):
    '''respond to all keypresses'''
    #ship keypress
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        
        #bullet keypress
        if event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


    #ship key releases
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False



def update_screen(ai_settings, screen, ship, bullets):
    '''Draw screen and elements'''
    screen.fill(ai_settings.bg_color)
    ship.draw_ship()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()
    #clock.tick(30)