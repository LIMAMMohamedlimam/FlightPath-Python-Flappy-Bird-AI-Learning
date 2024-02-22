import pygame , time
from models import Disc , Bar
from config import *

class Game():
    def __init__(self):
        self.disc = Disc()
        self.bars = []
        self.clock = pygame.time.Clock()
        self.score = 0
        self.game_over = False
        self.start_time = None #clock

    def reset(self):
        self.disc.reset()
        self.bars = []
        self.score = 0
        self.game_over = False
        self.start_time = time.time()

    def display_score(self , screen , SCORE_FONT):
        timepassed = int(time.time() - self.start_time) #temp écouler
        score_text = f"Score : {self.score} Time : {timepassed}" #score
        score_surface = SCORE_FONT.render(score_text , True , GREEN) 
        screen.blit(score_surface, [5,5])

    def run(self , screen ):
        running = True
        self.start_time = time.time() #Initialisation du conteur 
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and not self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.disc.flap()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.disc.flap()

            screen.fill(WHITE)

            if not self.game_over:
                self.disc.update()

                if len(self.bars) == 0 or self.bars[-1].x < SCREEN_WIDTH - 300:
                    self.bars.append(Bar())

                for bar in self.bars:
                    bar.update()

                self.bars = [bar for bar in self.bars if not bar.off_screen()]

                for bar in self.bars:
                    if bar.collide(self.disc):
                        self.game_over = True
                    if not bar.passed and bar.x < self.disc.x:
                        bar.passed = True
                        self.score += 1

                if self.disc.y <= 0 or self.disc.y >= SCREEN_HEIGHT:
                    self.game_over = True

            self.disc.draw(screen)
            for bar in self.bars:
                bar.draw(screen)

            self.display_score(screen , pygame.font.SysFont('Arial' , 20))

            if self.game_over:
                self.reset()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()