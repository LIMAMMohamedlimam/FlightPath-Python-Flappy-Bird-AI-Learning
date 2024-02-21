
import time
import pygame
import random
from game import Game
from config import SCREEN_HEIGHT , SCREEN_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    game = Game()
    game.run(screen)
    pygame.quit()


if  __name__ == "__main__":
    main()