import pygame
import thorpy

windowWidth, windowHeight, windowScaleFactor = 500, 500, 10

class App:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((windowWidth, windowHeight + 20))
        self.gameClock = pygame.time.Clock()
        self.gameFont = pygame.font.SysFont('Arial', 20)
        self.infoText = self.gameFont.render('For menu/reset press [R]', False, (255, 255, 255))
        self.lastChoice = None
        self.cWidth = int(windowScaleFactor - windowScaleFactor * 0.3)
        self.cHeight = self.cWidth
        self.window.fill((100, 100, 100))
        self.drawGrid()
        self.buttons = [
            thorpy.make_button("random", func=self.reactMainMenuButtonPressed, params={'choice': 'random'}),
            thorpy.make_button("custom", func=self.reactMainMenuButtonPressed, params={'choice': 'custom'})
        ]
        self.menuBox = thorpy.Box(elements=self.buttons)
        thorpy.store(self.menuBox, mode='h', gap=20)
        self.menuBox.fit_children()
        self.menu = thorpy.Menu(self.menuBox)
        for e in self.menu.get_population():
            e.surface = self.window
        self.menuBox.set_center((windowWidth/2, windowHeight/2))

    def reactMainMenuButtonPressed(self, choice):
        self.lastChoice = choice

    def setText(self, text: str):
        self.infoText = self.gameFont.render(text, False, (255, 255, 255))

    def drawGrid(self):
        for i in range(0, windowWidth, windowScaleFactor):
            pygame.draw.line(self.window, (150, 150, 150), (i, 0), (i, windowHeight))
        for i in range(0, windowHeight, windowScaleFactor):
            pygame.draw.line(self.window, (150, 150, 150), (0, i), (windowWidth, i))

    def showMenu(self):
        pygame.display.flip()
        self.menuBox.blit()
        self.menuBox.update()
        self.window.blit(self.infoText, (0, windowHeight))

    def drawCursor(self, x, y):
        cX = int(x * windowScaleFactor + windowScaleFactor * 0.2)
        cY = int(y * windowScaleFactor + windowScaleFactor * 0.2)
        rect = pygame.Rect(cX, cY, self.cWidth, self.cHeight)
        pygame.draw.rect(self.window, (0, 250, 0), rect)
        pygame.display.flip()

    def redrawCells(self, cells: list[(int, int)]):
        self.window.fill((100, 100, 100))
        self.drawGrid()
        for c in cells:
            cX = int(c[0] * windowScaleFactor + windowScaleFactor * 0.2)
            cY = int(c[1] * windowScaleFactor + windowScaleFactor * 0.2)
            rect = pygame.Rect(cX, cY, self.cWidth, self.cHeight)
            pygame.draw.rect(self.window, (250, 0, 0), rect)
        self.window.blit(self.infoText, (0, windowHeight))
        pygame.display.flip()



