
import time , neat
import pygame
import random
import os
from game import Game
from config import SCREEN_HEIGHT , SCREEN_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    game = Game()
    game.run(screen)
    pygame.quit()


def run_ai(config_path):
    config = neat.config.Config(neat.DefaultGenome , neat.DefaultReproduction ,
                                neat.DefaultSpeciesSet , neat.DefaultStagnation,
                                config_path)
    
    popul = neat.Population(config)
    popul.add_reporter(neat.StdOutReporter(True))
    status = neat.StatisticsReporter()
    popul.add_reporter(status)

    #winner = popul.run( ,50)


if  __name__ == "__main__":
    local_dir  = os.path.dirname(__file__)
    config_path = os.path.joi,(local_dir,'NeatConfig.txt')
    run_ai(config_path)
    main()