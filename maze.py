from cmu_graphics import *
import random
from helper import *
################################################################################
# class Maze is for defining and drawing maze
# the maze(simple version) is consisted of path and wall
# reference: https://github.com/sbhotika/15112-term-project/blob/master/Maze.py
# reference: https://en.wikipedia.org/wiki/A*_search_algorithm
################################################################################

class Maze:
    # def defaultMaze(difficulty,value = None):
    #     deMaze = []
    #     for row in range(difficulty * 4):
    #         for col in range(difficulty * 4):
    #             deMaze += [value * difficulty * 4]
    #     return deMaze
    
    def __init__(self,difficulty):
        #difficulty input should be int from 1 to 5
        # self.size = size
        self.difficulty = difficulty
        self.rows = self.difficulty * 4 + 1
        self.cols = self.difficulty * 4 + 1
        self.tile = 50
        # self.maze = [[0]*self.rows for i in range(self.cols)]

        self.grid = [mazeGrid(x + 2, y + 2, self.tile) for y in range(self.rows) for x in range(self.cols)]
        
        self.entrance = None
        self.exit = None
        # self.board = Maze.defaultMaze
        # maze border
        # for i in range(self.rows):
        #     self.maze[i][0] = self.maze[i][self.rows - 1] = 0
        # for j in range(self.cols):
        #     self.maze[0][j] = self.maze[self.cols - 1][j] = 0
        

    def generate(self):
        # maze generation algorithm Depth-First Search

        def isSolution(gridCells, currCell):
            currCell.visited = True
            nextCell = currCell.isNeighborLegal(gridCells)

            while neigborCell:
                getPath(currCell, nextCell)
                isSolution(self.grid, currCell)
                neigborCell = currCell.isNeighborLegal(self.grid)
    
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
        
        curr = self.grid[0]
        visitedCell = []

        # if next:
        #     next.visited = True
        #     visitedCell.append(curr)
        #     getPath(curr, next)
        #     curr = next
        # elif len(visitedCell) != 0:
        #     curr = visitedCell.pop()
        
        # return self.grid
        count = 1

        while len(self.grid) != count:
            curr.visited = True
            next = curr.isNeighborLegal(self.grid)
            if next:
                next.visited = True
                count += 1
                visitedCell.append(curr)
                getPath(curr, next)
                curr = next
            elif visitedCell:
                curr = visitedCell.pop()
        return self.grid


        

    
    


    #         def dfs(x, y):
    #                 dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #                 random.shuffle(dir)

    #                 for dx, dy in dir:
    #                     nx = x + 2 * dx
    #                     ny = y + 2 * dy
    #                     if (0 <= nx < self.rows 
    #                         and 0 <= ny < self.cols 
    #                         and self.maze[nx][ny] == 0):

    #                         self.maze[x + dx][y + dy] = 1
    #                         self.maze[nx][ny] = 1
    #                         dfs(nx, ny)
            
    #         # generate maze
    #         startX = random.randrange(1, self.rows, 2)
    #         startY = random.randrange(1, self.cols, 2)
    #         self.maze[startX][startY] = 1
    #         dfs(startX, startY)
    #         #set entrance and exit
    #         self.entrance = (1, 1) 
    #         self.exit = (self.rows - 2, self.cols - 2) 

    #         #check if there is a legal path from entrance to exit
    #         if self.findPath(self.entrance, self.exit):
    #             break

    # # findPath not finish, comment the entire check legal part to test the rest
    # def findPath(self, start, end):
    #     def heuristic(a, b):
    #         return abs(a[0] - b[0]) + abs(a[1] - b[1])

    #     def reconstructPath(prev, curr):
    #         path = [curr]
    #         while curr in prev:
    #             curr = prev[curr]
    #             path.append(curr)
    #         return path[::-1]

    #     openSet = [(heuristic(start, end), start)]
    #     prev = {}
    #     gScore = {start: 0}
    #     fScore = {start: heuristic(start, end)}

    #     while openSet:
    #         curr = min(openSet, key=lambda x: x[1])[0]
    #         openSet.remove((curr, fScore[curr]))

    #         if curr == end:
    #             return reconstructPath(prev, curr)

    #         for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #             neighbor = curr[0] + dx, curr[1] + dy
    #             if (0 <= neighbor[0] < self.width and 
    #                 0 <= neighbor[1] < self.height and 
    #                 self.maze[neighbor[0]][neighbor[1]] == 1):

    #                 score= gScore[curr] + 1
    #                 if score < gScore.get(neighbor, float('inf')):
    #                     prev[neighbor] = curr
    #                     gScore[neighbor] = score
    #                     fScore[neighbor] = score + heuristic(neighbor, end)
    #                     openSet.append((neighbor, fScore[neighbor]))
    #     return None 


    def isWall(self,x,y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.maze[x][y] == 0
        return False
    
    def render2D(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 1:
                    drawRect()
                if (i, j) == self.entrance:
                    drawRect()
                if (i, j) == self.exit:
                    drawRect()

    def __str__(self):
        return 
    
    def __hash__(self):
        return hash(self._)
    
    def __eq__(self, other):
        return (isinstance(other, Maze) and
                self._ == other._)
    

    def draw(self):
        for row in self.maze:
            for cell in row:
                if cell == 0:
                    print('#', end = ' ')
                else:
                    print(' ', end = ' ')
            print()

# test = Maze(3)
# test.generate()
# test.draw()

def onAppStart(app):
    app.width = 1000
    app.height = 800
    # app.tile = 50
    # app.cols= (app.width - 200) // app.tile
    # app.rows = (app.height - 200) // app.tile
    # app.m1 = mazeGrid(2,2)
    # startPX = (app.width/2 - app.cols * app.tile/2)
    # startPY = app.height/2 - app.rows * app.tile/2
    app.maze = Maze(3)
    # app.grid = [mazeGrid(x + 2, y + 2, app.tile) for y in range(app.rows) for x in range(app.cols)]

def redrawAll(app): 
    # myMaze = Maze(3)
    app.maze.generate()
    # for item in app.grid:
    #     item.draw()
        


def main():
    runApp()

# if __name__ == '__main__':
main()