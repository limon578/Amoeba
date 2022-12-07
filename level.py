import pygame
import sprites



def level(game):
    ''' Отрисовка меню уровней и обработка данных уровней сложности '''
    main_button = sprites.Button(400, 640, 'Main menu', game.middle_font)
    hard_button = sprites.Button(400, 480, 'Hard', game.middle_font)
    medium_button = sprites.Button(400, 400, 'Medium', game.middle_font)
    easy_button = sprites.Button(400, 320, 'Easy', game.middle_font)

    menu_run = True
    while menu_run:

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                return 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_button.be_inside(pos[0], pos[1]):
                    return 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard_button.be_inside(pos[0], pos[1]):
                    return 30
            if event.type == pygame.MOUSEBUTTONDOWN:
                if medium_button.be_inside(pos[0], pos[1]):
                    return 80
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.be_inside(pos[0], pos[1]):
                    return 150

        main_button.update(pos[0], pos[1])
        hard_button.updatel(pos[0], pos[1])
        medium_button.updatel(pos[0], pos[1])
        easy_button.updatel(pos[0], pos[1])

        game.screen.fill((127, 255, 212))
        game.draw_overlay()
    

        game.screen.blit(main_button.image, main_button.rect)
        game.screen.blit(hard_button.image, hard_button.rect)
        game.screen.blit(medium_button.image, medium_button.rect)
        game.screen.blit(easy_button.image, easy_button.rect)
        pygame.display.flip()

        game.clock.tick(20)
