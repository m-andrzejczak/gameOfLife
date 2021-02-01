import model
import view
import pygame
import sys
import random

a = view.App()
cursor = model.Cursor

def init(type: str):
    global cursor
    for i, x in enumerate(range(0, int(view.windowWidth/view.windowScaleFactor))):
        model.cellMap.append([])
        for y in range(0, int(view.windowHeight/view.windowScaleFactor)):
            model.cellMap[x].append(model.Cell(x,y))
    if type == 'random':
        x = random.randint(1, view.windowWidth/view.windowScaleFactor - 2)
        y = random.randint(1, view.windowHeight/view.windowScaleFactor - 2)
        initTable = model.NEIGHBOUR_OFFSETS[:]
        initCells = [(x, y)]
        for i in range(random.randint(3,8)):
            offset = initTable.pop(random.randint(0, len(initTable) - 1))
            cell = (x + offset[0], y + offset[1])
            initCells.append(cell)
            model.cellMap[cell[0]][cell[1]].alive = True
        a.redrawCells(initCells)
        a.setText('For menu/reset press [R]')
    elif type == 'custom':
        cursor = model.Cursor(int(view.windowWidth/view.windowScaleFactor), int(view.windowHeight/view.windowScaleFactor))
        a.setText('[Arrows] move cursor, [Space] choose, [Enter] start')
    elif type == 'custom_reinit':
        for cell in cursor.chosenCells:
            model.cellMap[cell[0]][cell[1]].alive = True
            a.setText('For menu/reset press [R]')

def gameStep():
    global cursor
    a.gameClock.tick(30)
    if model.gameInProgress:
        if a.lastChoice == 'custom':
            a.redrawCells(cursor.chosenCells)
            a.drawCursor(cursor.x, cursor.y)
        else:
            a.redrawCells(model.updateGrid())
    else:
        a.showMenu()
        if a.lastChoice:
            model.gameInProgress = True
            init(a.lastChoice)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                model.gameInProgress = False
                model.cellMap = [[]]
                a.lastChoice = None
                try:
                    del cursor
                except:
                    pass
            if a.lastChoice == 'custom':
                if e.key == pygame.K_UP:
                    cursor.moveUp()
                elif e.key == pygame.K_DOWN:
                    cursor.moveDown()
                elif e.key == pygame.K_LEFT:
                    cursor.moveLeft()
                elif e.key == pygame.K_RIGHT:
                    cursor.moveRight()
                elif e.key == pygame.K_SPACE:
                    cursor.addOrRemove()
                elif e.key == pygame.K_RETURN:
                    a.lastChoice = None
                    init('custom_reinit')
        if not model.gameInProgress:
            a.menu.react(e)
