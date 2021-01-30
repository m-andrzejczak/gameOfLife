import model
import view
import pygame
import sys
import random

a = view.App()

def init():
    for i, x in enumerate(range(0, int(view.windowWidth/view.windowScaleFactor))):
        model.cellMap.append([])
        for y in range(0, int(view.windowHeight/view.windowScaleFactor)):
            model.cellMap[x].append(model.Cell(x,y))
    x = random.randint(1, view.windowWidth/view.windowScaleFactor - 2)
    y = random.randint(1, view.windowHeight/view.windowScaleFactor - 2)
    initTable = model.NEIGHBOUR_OFFSETS[:]
    initCells = [(x, y)]
    for i in range(random.randint(3,8)):
        offset = initTable.pop(random.randint(0, len(initTable) - 1))
        cell = (x + offset[0], y + offset[1])
        initCells.append(cell)
        model.cellMap[cell[0]][cell[1]].alive = True

def gameStep():
    a.redrawCells(model.updateGrid())
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)