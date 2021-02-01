class Cell:
    global cellMap
    global NEIGHBOUR_OFFSETS

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False

    def getInfo(self):
        print(str(self.x) + ' ' + str(self.y))

    def genNeighbours(self):
        for n in NEIGHBOUR_OFFSETS:
            newX = self.x + n[0]
            newY = self.y + n[1]
            if newX < 0 or newX > (len(cellMap) - 2) or newY < 0 or newY > (len(cellMap[0]) - 1):
                continue
            else:
                yield newX, newY

    def checkNeighbours(self):
        countAlive = 0
        for neighbour in self.genNeighbours():
            n_x, n_y = neighbour
            try:
                if cellMap[n_x][n_y].alive:
                    countAlive += 1
            except IndexError as e:
                print(e.args)
        return countAlive

    def refreshStatus(self):
        neighboursAlive = self.checkNeighbours()
        if neighboursAlive == 3:
            self.alive = True
        elif neighboursAlive < 2 or neighboursAlive > 3:
            self.alive = False
        return self.alive

class Cursor:
    def __init__(self, gridWidth: int, gridHeight: int):
        self.x = 0
        self.y = 0
        self.chosenCells = []
        self.gridDimensions = (gridWidth, gridHeight)

    def addOrRemove(self):
        tmp = (self.x, self.y)
        if (self.x, self.y) in self.chosenCells:
            self.chosenCells.remove(tmp)
        else:

            self.chosenCells.append(tmp)

    def moveDown(self):
        if self.y < self.gridDimensions[1]:
            self.y += 1
        return self.x, self.y

    def moveUp(self):
        if self.y > 0:
            self.y -= 1
        return self.x, self.y

    def moveLeft(self):
        if self.x > 0:
            self.x -= 1
        return self.x, self.y

    def moveRight(self):
        if self.x < self.gridDimensions[0]:
            self.x += 1
        return self.x, self.y


cellMap = [[]]
NEIGHBOUR_OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
gameInProgress = False

def updateGrid() -> list[(int, int)]:
    aliveCells = []
    for i in range(len(cellMap) - 1):
        for cell in cellMap[i]:
            if cell.refreshStatus():
                aliveCells.append((cell.x, cell.y))
    return aliveCells
