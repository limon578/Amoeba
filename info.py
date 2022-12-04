import pygame
import sprites



def info(game):
    main_button = sprites.Button(400, 540, 'Main menu', game.middle_font)

    menu_run = True
    while menu_run:

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                return 200
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_button.be_inside(pos[0], pos[1]):
                    return 200

        main_button.update(pos[0], pos[1])

        game.screen.fill((127, 255, 212))
        game.draw_overlay()
        game.draw_author()

        game.screen.blit(main_button.image, main_button.rect)
        
        pygame.display.flip()

        game.clock.tick(20)
