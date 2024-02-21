import pygame , random
from config import *


class Disc:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.vel = 0

    def draw(self , screen ):
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

    def draw(self , screen ):
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
