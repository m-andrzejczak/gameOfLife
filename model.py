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
        elif neighboursAlive < 2 or neighboursAlive > 4:
            self.alive = False
        return self.alive

cellMap = [[]]
NEIGHBOUR_OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def updateGrid() -> list[(int, int)]:
    aliveCells = []
    for i in range(len(cellMap) - 1):
        for cell in cellMap[i]:
            if cell.refreshStatus():
                aliveCells.append((cell.x, cell.y))
    return aliveCells
