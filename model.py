class Cell:
    global cellMap

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False

    def getInfo(self):
        print(str(self.x) + ' ' + str(self.y))

    def genNeighbours(self):
        for h_offset in range(-1, 1):
            for y_offset in range(-1, 1):
                if h_offset != 0 and y_offset != 0:
                    yield self.x + h_offset, self.y + y_offset
    # TODO check generator
    def checkNeighbours(self):
        countAlive = 0
        for neighbour in self.genNeighbours():
            n_x, n_y = neighbour
            # print(str(self.x) + ' ' + str(self.y) + ' ' + str(n_x) + ' ' + str(n_y))
            try:
                if cellMap[n_x][n_y].alive:
                    countAlive += 1
            except IndexError:
                pass
        if countAlive > 0:
            print(countAlive)
        return countAlive

    def refreshStatus(self):
        oldStatus = self.alive
        neighboursAlive = self.checkNeighbours()
        if neighboursAlive == 3:
            self.alive = True
        elif neighboursAlive < 2 or neighboursAlive > 4:
            self.alive = False
        if oldStatus != self.alive:
            return 1
        return 0

cellMap = [[]]

def updateGrid() -> list[(int, int)]:
    cellsChanged = []
    for i in range(len(cellMap)):
        for cell in cellMap[i]:
            if cell.refreshStatus():
                cellsChanged.append((cell.x, cell.y))
    return cellsChanged
