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
            # Открытие главного меню
            t = menu(g)

        if t == 1:
            # Открытие меню info
            t = info(g)

        if t == 2:
            # Открытие меню level
            t = level(g)
      
        if t == 30:
            # Уровень сложности Hard
            t = g.game(30)
            t = t and menu(g)
        
        if t == 80:
            # Уровень сложности Medium
            t = g.game(80)
            t = t and menu(g)
         
        if t == 150:
            # Уровень сложности Easy
            t = g.game(150)
            t = t and menu(g)
         
        if t == 140:
            # Уровень сложности Play (обычынй)
            t = g.game(140)
            t = t and menu(g)

    pygame.quit()

