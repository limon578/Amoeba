import pygame
import sprites



def menu(game):
    play_button = sprites.Button(400, 550, 'Play', game.middle_font)
    level_button = sprites.Button(400, 690, 'level', game.middle_font)
    info_button = sprites.Button(400, 620, 'Info', game.middle_font)

    menu_run = True
    while menu_run:

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.be_inside(pos[0], pos[1]):
                    return 15
                if info_button.be_inside(pos[0], pos[1]):                    
                    return 100
                if level_button.be_inside(pos[0], pos[1]):
                    return 300

        play_button.update(pos[0], pos[1])
        info_button.update(pos[0], pos[1])
        level_button.update(pos[0], pos[1])
        
        game.screen.fill((127, 255, 212))
        game.draw_overlay()
        game.draw_menu_header()
        
        game.screen.blit(play_button.image, play_button.rect)
        
        game.screen.blit(info_button.image, info_button.rect)
        game.screen.blit(level_button.image, level_button.rect)

        pygame.display.flip()

        game.clock.tick(20)
