import pygame
from game import Game
from menu import menu
from info import info
from level import level

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    g = Game(screen)
 
    t = menu(g)
    
    while t is not False:
        if t == 3:
            t = menu(g)

        if t == 1:
            t = info(g)

        if t == 2:
            t = level(g)

        if t == 30:
            t = g.game(30)
            t = t and menu(g)
       
        if t == 80:
            t = g.game(80)
            t = t and menu(g)

        if t == 150:
            t = g.game(150)
            t = t and menu(g)

        if t == 140:
            t = g.game(140)
            t = t and menu(g)

    pygame.quit()
