import pygame
import thorpy

windowWidth, windowHeight, windowScaleFactor = 500, 500, 10

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((windowWidth, windowHeight))
        self.gameClock = pygame.time.Clock()
        self.lastChoice = None
        self.window.fill((100, 100, 100))
        self.drawGrid()
        self.images = [
            pygame.image.load(r'img/1.png'),
            pygame.image.load(r'img/2.png'),
            pygame.image.load(r'img/3.png')
        ]
        self.buttons = [
            thorpy.make_button("1", func=self.reactMainMenuButtonPressed, params={'choice': '1'}),
            thorpy.make_button("2", func=self.reactMainMenuButtonPressed, params={'choice': '2'}),
            thorpy.make_button("3", func=self.reactMainMenuButtonPressed, params={'choice': '3'})
        ]
        self.menuBox = thorpy.Box(elements=self.buttons)
        thorpy.store(self.menuBox, mode='h', gap=80)
        self.menuBox.fit_children()
        self.menu = thorpy.Menu(self.menuBox)
        for e in self.menu.get_population():
            e.surface = self.window
        self.menuBox.set_center((windowWidth/2, windowHeight/2 + 20))

    def reactMainMenuButtonPressed(self, choice):
        self.lastChoice = choice

    def drawGrid(self):
        for i in range(0, windowWidth, windowScaleFactor):
            pygame.draw.line(self.window, (150, 150, 150), (i, 0), (i, windowHeight))
        for i in range(0, windowHeight, windowScaleFactor):
            pygame.draw.line(self.window, (150, 150, 150), (0, i), (windowWidth, i))

    def showMenu(self):
        for i, img in enumerate(self.images):
            self.window.blit(img, (i * 90 + windowWidth/2 - (len(self.images) * 90)/2 + 20, windowHeight/2 - img.get_rect().size[1]))
        pygame.display.flip()
        self.menuBox.blit()
        self.menuBox.update()

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



