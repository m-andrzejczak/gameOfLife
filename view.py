import sys
import pygame
import thorpy
from model import Cell

gameOn = True

class App:
    width, height = 500, 500
    scale = 2

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((100, 100, 100))
        for i in range(0, self.width, 10):
            pygame.draw.line(self.window, (150, 150, 150), (i, 0), (i, self.height))
        for i in range(0, self.height, 10):
            pygame.draw.line(self.window, (150, 150, 150), (0, i), (self.width, i))
        pygame.display.flip()

    def gameStep(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
