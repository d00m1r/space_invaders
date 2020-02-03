"""contained all main functions for game process"""
import sys
import pygame

from time import sleep
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, sb, ship, aliens, bullets)

        if stats.game_active:
            #spaceship moving
            check_keypress_events(event, ship, screen, bullets, ai_settings)

def check_keypress_events(event, ship, screen, bullets, ai_settings):
    '''respond to all keypresses'''
    #keypress
    if event.type == pygame.KEYDOWN:
        #quit
        if event.key == pygame.K_q:
            sys.exit()
        
        #ship keypress
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        
        #bullet keypress
        if event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            if len(bullets) < ai_settings.bullet_limit:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)

    #ship key releases
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, sb, ship, aliens, bullets):
    '''start a new game when the player clicks Play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset the game settings
        ai_settings.initialize_dynamic_settings()
        
        #hide the mouse cursor
        pygame.mouse.set_visible(False)

        #reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        #reset the scoreboard images
        stats.score = 0
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_lvl()
        sb.prep_ships()
        
        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        
        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def create_fleet(ai_settings, screen, ship, aliens):
    '''Create a full fleet of aliens'''
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    ship_height = ship.rect.height
    available_space_x = ai_settings.screen_wigth - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    number_rows = get_number_rows(ai_settings, ship_height, alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    
def get_number_rows(ai_settings, ship_height, alien_height):
    '''determine the number of rows of aliens that fit on the screen'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''create a single alien'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''respond to bullet-alien collisions'''
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        stats.score += ai_settings.alien_points
        sb.prep_score()   
    check_high_score(stats, sb)

    #kill all and go to the next lvl
    if len(aliens) == 0:
        go_next_lvl(ai_settings, screen, stats, sb, ship, aliens, bullets)

def go_next_lvl(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #destroy existing bullets and create new fleet
    bullets.empty()
    
    #speed up game
    ai_settings.increase_speed()
    create_fleet(ai_settings, screen, ship, aliens) 

    stats.lvl += 1
    sb.prep_lvl()

def update_bullets(aliens, bullets, ai_settings, screen, stats, sb, ship):
    #calls bullet.update() for each bullet we place in the group bullets
        bullets.update()

        #get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                
        check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''check if any aliens have reached the bottom of the screen'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''update the positions of all aliens in the fleet'''
    check_fleet_edges(ai_settings, aliens)  
    aliens.update()

    #look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    #look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''Respond to ship being hit by alien'''
    if stats.ships_left > 1:
        #decrement ships_left
        stats.ships_left -= 1

        #update scoreboard
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(1)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False

def check_fleet_edges(ai_settings, aliens):
    '''respond appropriately if any aliens have reached and edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''drop the entire fleet and change the fleet's direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
    '''check to see if there's a new high score'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    
def update_screen(ai_settings, stats, screen, sb, ship, bullets, aliens, play_button):
    '''draw screen and elements'''
    screen.fill(ai_settings.bg_color)

    if stats.game_active:
        ship.draw_ship()
        aliens.draw(screen)
    
        #redraw all bullets behind ship and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        #draw the score information
        sb.show_score()

    #game is inactive
    else:
        play_button.draw_button()

    pygame.display.flip()
    #clock.tick(30)