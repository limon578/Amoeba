import pygame
import sprites



def menu(game):
    play_button = sprites.Button(400, 540, 'Play', game.middle_font)

    info_button = sprites.Button(400, 640, 'Info', game.middle_font)

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

        play_button.update(pos[0], pos[1])
        info_button.update(pos[0], pos[1])

        
        game.screen.fill((127, 255, 212))
        game.draw_overlay()
        game.draw_menu_header()
        
        game.screen.blit(play_button.image, play_button.rect)
        
        game.screen.blit(info_button.image, info_button.rect)

        pygame.display.flip()

        game.clock.tick(20)
