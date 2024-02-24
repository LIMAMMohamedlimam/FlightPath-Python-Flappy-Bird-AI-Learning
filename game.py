import pygame , time , neat
from models import Disc , Bar
from config import *

class Game():
    def __init__(self):
        
        self.discs = []
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

    def run(self , screen , genomes , config ):
        gen = []
        nets = []

        for g in genomes :
            net  = neat.nn.FeedForwardNetwork(g, config)
            nets.append(net)
            self.discs.append(Disc())
            g.fitness = 0
            gen.append(g)


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
                for disc in self.discs :
                    disc.update()

                if len(self.bars) == 0 or self.bars[-1].x < SCREEN_WIDTH - 300:
                    self.bars.append(Bar())

                for bar in self.bars:
                    bar.update()

                self.bars = [bar for bar in self.bars if not bar.off_screen()]
                #self.discs = [disc for ]

                for bar in self.bars:
                    for x ,disc in enumerate(self.discs) :
                        if bar.collide(disc):
                            #self.game_over = True
                            gen[x].fitness -= 1 
                            self.discs.pop(x)
                            net.pop(x)
                            gen.pop(x)

                        if not bar.passed and bar.x < disc.x:
                            bar.passed = True
                            self.score += 1
                for disc in self.discs :
                    if disc.y <= 0 or disc.y >= SCREEN_HEIGHT:
                        pass
            for disc in self.discs:
                disc.draw(screen)
            for bar in self.bars:
                bar.draw(screen)

            self.display_score(screen , pygame.font.SysFont('Arial' , 20))

            if self.game_over:
                self.reset()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()