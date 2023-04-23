from cmu_graphics import *
import random

# RES = WIDTH, HEIGHT = 1202, 902
# TILE = 100
# cols, rows = WIDTH // TILE, HEIGHT // TILE
## define the canvas size
## define single grid size
## calculate cols and rows numbers
##  


class mazeGrid:
    #initialize the maze, x is the number of rows, y is the number of cols
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile
        self.wall = {'up':True, 'down':True, 'right':True, 'left': True}
        self.visited = False
        self.gridWidth = 4

    def draw(self):
        #find the left top point for each cell
        xPosi = self.x * self.tile
        yPosi = self.y * self.tile

        if self.wall['up']:
            drawLine(xPosi, yPosi, xPosi + self.tile, yPosi, lineWidth = self.gridWidth)
        if self.wall['down']:
            drawLine(xPosi, yPosi + self.tile, xPosi + self.tile, yPosi + self.tile, lineWidth = self.gridWidth)
        if self.wall['left']:
            drawLine(xPosi, yPosi, xPosi, yPosi + self.tile, lineWidth = self.gridWidth)
        if self.wall['right']:
            drawLine(xPosi + self.tile, yPosi, xPosi + self.tile, yPosi + self.tile, lineWidth = self.gridWidth)
    
    def getCellBorder(self):
        cellBorder = []
        xPosi = self.x * self.tile
        yPosi = self.y * self.tile
        #left
        if self.wall['up']:
            cellBorder.append(drawRect(xPosi, yPosi, self.tile, self.gridWidth))
        if self.wall['down']:
            cellBorder.append(drawRect(xPosi, yPosi + self.tile, self.tile, self.gridWidth))
        if self.wall['left']:
            cellBorder.append(drawRect(xPosi, yPosi + self.tile, self.gridWidth, self.tile))
        if self.wall['right']:
            cellBorder.append(drawRect(xPosi + self.tile, yPosi, self.gridWidth, self.tile))
        return cellBorder
    
    def isLegalCell(self, x, y):
        ## x is the rowIndex of the cell in the mazeGrid, y is the colIndex of the cell
        def getCellIndex(x,y):
            index = x + y * self.y
            return index
        if x < 0 or y < 0 or x > self.x -1 or y > self.y -1:
            return False
        else:
            return self.gridCells[getCellIndex(x, y)]
        
    def legalNeighbor(self, gridCells):
        self.gridCells = gridCells
        neighbors = []
        top = self.isLegalCell(self.x, self.y - 1)
        right = self.isLegalCell(self.x + 1, self.y)
        bottom = self.isLegalCell(self.x, self.y + 1)
        left = self.isLegalCell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False
    
        # dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # neigbors = []
        # for dx, dy in dir:
        #     neigbor = self.isLegalCell(self.x + dx, self.y + dy)
        #     if neigbor and not neigbor.visited:
        #         neigbors.append(neigbor)
            
        #     if neigbors:
        #         return random.choice(neigbors)
        #     else:
        #         return False

def getPath(curr, next):
    dx = curr.x - next.x
    dy = curr.y - next.y
    if dx == 1:
        curr.wall['left'] = False
        next.wall['right'] = False
    elif dx == -1:
        curr.wall['right'] = False
        next.wall['left'] = False    
    elif dy == 1:
        curr.wall['up'] = False
        next.wall['down'] = False                               
    elif dy == -1:
        curr.wall['down'] = False
        next.wall['up'] = False   




def onAppStart(app):
    app.width = 1000
    app.height = 800
    app.tile = 50
    app.cols= (app.width - 200) // app.tile
    app.rows = (app.height - 200) // app.tile
    # app.m1 = mazeGrid(2,2)
    startPX = (app.width/2 - app.cols * app.tile/2)
    startPY = app.height/2 - app.rows * app.tile/2
    app.grid = [mazeGrid(x + 2, y + 2, app.tile) for y in range(app.rows) for x in range(app.cols)]

      


def redrawAll(app): 
    # generate(app.grid)
    # for item in app.grid:
    #     item.draw()
    def generate():
        grid = app.grid
        curr = grid[0]
        visitedCell = []
        count = 1

        while len(grid) != count:
            curr.visited = True
            next = curr.legalNeighbor(grid)
            if next:
                next.visited = True
                count += 1
                visitedCell.append(curr)
                getPath(curr, next)
                curr = next
            elif visitedCell:
                curr = visitedCell.pop()
        return grid  
    
    for item in generate():
        item.draw()
        


def main():
    runApp()

# if __name__ == '__main__':
main()
