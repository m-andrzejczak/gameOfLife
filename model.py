class Cell:
    global cellMap
    alive = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def genNeighbours(self):
        for h_offset in range(-1, 1):
            for y_offset in range(-1, 1):
                if h_offset != 0 and y_offset != 0:
                    yield self.x + h_offset, self.y + y_offset

    def checkNeighbours(self):
        countAlive = 0
        for neighbour in self.genNeighbours():
            n_x, n_y = neighbour
            if cellMap[n_x][n_y].alive:
                countAlive += 1
        return countAlive

    def refreshStatus(self):
        neighboursAlive = self.checkNeighbours()
        if neighboursAlive == 3:
            self.alive = True
        elif neighboursAlive < 2 or neighboursAlive > 4:
            self.alive = False

cellMap = [[Cell]]