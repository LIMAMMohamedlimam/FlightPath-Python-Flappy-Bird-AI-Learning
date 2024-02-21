# game_oop.py
import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Game constants
GRAVITY = 0.25
FLAP_POWER = -5
BAR_WIDTH = 70
GAP_SIZE = 150
BAR_VELOCITY = -4
FPS = 60



class Disc:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.vel = 0

    def draw(self):
        pygame.draw.circle(screen, GREEN, (self.x, int(self.y)), 20)

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def flap(self):
        self.vel = FLAP_POWER

    def reset(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.vel = 0

class Bar:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.top = 0
        self.bottom = 0
        self.passed = False
        self.set_height()

    def set_height(self):
        self.top = random.randint(SCREEN_HEIGHT // 4, 3 * SCREEN_HEIGHT // 4)
        self.bottom = self.top + GAP_SIZE

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, BAR_WIDTH, self.top))
        pygame.draw.rect(screen, GREEN, (self.x, self.bottom, BAR_WIDTH, SCREEN_HEIGHT))

    def update(self):
        self.x += BAR_VELOCITY

    def off_screen(self):
        return self.x < -BAR_WIDTH

    def collide(self, disc):
        disc_rect = pygame.Rect(disc.x - 20, disc.y - 20, 40, 40)
        top_rect = pygame.Rect(self.x, 0, BAR_WIDTH, self.top)
        bottom_rect = pygame.Rect(self.x, self.bottom, BAR_WIDTH, SCREEN_HEIGHT)
        return top_rect.colliderect(disc_rect) or bottom_rect.colliderect(disc_rect)

class Game:
    def __init__(self):
        self.disc = Disc()
        self.bars = []
        self.clock = pygame.time.Clock()
        self.score = 0
        self.game_over = False

    def reset(self):
        self.disc.reset()
        self.bars = []
        self.score = 0
        self.game_over = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and not self.game_over:
                    if event.key == pygame.K_SPACE:
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

            self.disc.draw()
            for bar in self.bars:
                bar.draw()

            if self.game_over:
                self.reset()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

game = Game()
game.run()
