import pygame
import thorpy

windowWidth, windowHeight, windowScaleFactor = 500, 500, 10

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((windowWidth, windowHeight))
        self.window.fill((100, 100, 100))
        self.drawGrid()

    def drawGrid(self):
        for i in range(0, windowWidth, windowScaleFactor):
            pygame.draw.line(self.window, (150, 150, 150), (i, 0), (i, windowHeight))
        for i in range(0, windowHeight, windowScaleFactor):
            pygame.draw.line(self.window, (150, 150, 150), (0, i), (windowWidth, i))

    def redrawCells(self, cells: list[(int, int)]):
        self.window.fill((100, 100, 100))
        self.drawGrid()
        cWidth = int(windowScaleFactor - windowScaleFactor * 0.3)
        cHeight = cWidth
        for c in cells:
            cX = int(c[0] * windowScaleFactor + windowScaleFactor * 0.2)
            cY = int(c[1] * windowScaleFactor + windowScaleFactor * 0.2)
            rect = pygame.Rect(cX, cY, cWidth, cHeight)
            pygame.draw.rect(self.window, (250, 0, 0), rect)
        pygame.display.flip()



