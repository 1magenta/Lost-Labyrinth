from cmu_graphics import *
import random
from settings import *
################################################################################
# class Maze is for defining and drawing maze
# use depth first search to generate maze
# reference: https://en.wikipedia.org/wiki/A*_search_algorithm
################################################################################

class Maze:
    
    def __init__(self,difficulty):
        #difficulty input should be int from 1 to 5
        # self.size = size
        self.difficulty = difficulty
        self.rows = self.difficulty * 2 + 3
        self.cols = self.difficulty * 2 + 3
        self.cellSize = GRIDSIZE
        self.maze = [[0]*self.cols for i in range(self.rows)]
        self.worldMap = {}
        # store the rowIdx and colIdx of entrance/exit as a tuple
        self.entrance = (0, 1) 
        self.exit = (self.rows - 1, self.cols - 2) 
        

    def generate(self):
        # while True:
        # maze generation algorithm Depth-First Search
        def dfs(x, y):
                dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                random.shuffle(dir)

                for dx, dy in dir:
                    nx = x + 2 * dx
                    ny = y + 2 * dy
                    if (0 <= nx < self.rows 
                        and 0 <= ny < self.cols 
                        and self.maze[nx][ny] == 0):

                        self.maze[x + dx][y + dy] = 1
                        self.maze[nx][ny] = 1
                        dfs(nx, ny)
        
        # generate maze
        startX = random.randrange(1, self.rows, 2)
        startY = random.randrange(1, self.cols, 2)
        self.maze[startX][startY] = 1
        dfs(startX, startY)
        
        #define entrance and exit as path, 0 is wall, 1 is path 
        self.maze[0][1] = 1
        self.maze[self.rows - 1][self.cols - 2] = 1
    

    def draw(self):
        rows = self.rows
        cols = self.cols
        for rowIdx in range(rows):
            for colIdx in range(cols):
                leftTopX = colIdx * self.cellSize + WIDTH / 2 - self.cols * self.cellSize / 2
                leftTopY = rowIdx * self.cellSize + HEIGHT / 2 - self.rows * self.cellSize / 2
                if self.entrance == (rowIdx, colIdx):
                    drawLabel("Start", leftTopX + self.cellSize/2, leftTopY + self.cellSize/2, 
                              fill = 'white', bold = True, size = 18)
                elif self.exit == (rowIdx, colIdx):
                    drawLabel("Exit", leftTopX + self.cellSize/2, leftTopY + self.cellSize/2,
                              fill = 'white', bold = True, size = 18)

                # 0 is wall, 1 is path 
                elif self.maze[rowIdx][colIdx] == 0:
                    # xPosi = colIdx * self.cellSize
                    # yPosi = rowIdx * self.cellSize
                    drawRect(leftTopX, leftTopY, self.cellSize, self.cellSize, fill = 'grey') 


# def onAppStart(app):
#     app.width = WIDTH
#     app.height = HEIGHT
#     app.difficulty = 4
#     app.maze = Maze(app.difficulty)

# def redrawAll(app): 
#     app.maze.generate()
#     app.maze.draw()


# def main():
#     runApp()

# # if __name__ == '__main__':
# main()
