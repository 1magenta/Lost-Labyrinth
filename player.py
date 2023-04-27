from cmu_graphics import *
import random
import math
from settings import *
################################################################################
# class player is for defining the player's position, movement
################################################################################

class Player:
    # level = 0
    def __init__(self, maze):
        self.maze = maze
        #initilize player defaut position, maze.entrance only store the index of row and col
        (self.y, self.x) = maze.entrance
        self.x += 0.5
        self.y += 0.5
        self.mazeMap = maze.maze
        self.mazeWidth = GRIDSIZE * maze.cols
        self.angle = initAngle
        self.step = 0.3
        self.legalMove = True
        self.win = False 
        self.score = 100

    def moveForward(self): #call this method by keyboard input                       
        newX = self.x + self.step * math.cos(math.radians(self.angle))
        newY = self.y + self.step * math.sin(math.radians(self.angle))
        self.checkCollision(newX, newY)
        # print(2, self.legalMove) 
        if self.legalMove:
            self.x, self.y = newX, newY


    def moveBackward(self): #call this method by keyboard input                        
        newX = self.x - self.step * math.cos(math.radians(self.angle))
        newY = self.y - self.step * math.sin(math.radians(self.angle))
        self.checkCollision(newX, newY)
        if self.legalMove:
            self.x, self.y = newX, newY

    def turnRight(self):
        self.angle += 15

    def turnLeft(self):
        self.angle -= 15
            
    def checkCollision(self, x, y):
        atRowIdx, atColIdx = int(y), int(x)
        mazeRows = self.maze.rows - 1
        mazeCols = self.maze.cols - 1
        if atRowIdx < 0 or atColIdx < 0 or atRowIdx > mazeRows or atColIdx > mazeCols:
            self.legalMove = False
        currCell = self.maze.maze[atRowIdx][atColIdx]
        # 0 is wall, 1 is path
        if currCell == 0:
            self.legalMove = False
        else:
                self.legalMove = True

    
    def youWin(self):

        (exitY, exitX) = self.maze.exit
        if self.y >= exitY and self.x >= exitX:
            self.win = True
            # level += 1

    def surroundingWalls(self):
        countWall = 0
        if (self.x + 1 < len(self.mazeMap) and self.y + 1 < len(self.mazeMap[0])
            and self.x - 1 > 0 and self.y - 1 > 0):
            frontColIdx, frontRowIdx = int(self.x), int(self.y) + 1
            backColIdx, backRowIdx = int(self.x), int(self.y) - 1
            leftColIdx, leftRowIdx = int(self.x) - 1, int(self.y)
            rightColIdx, rightRowIdx = int(self.x) + 1, int(self.y)

            if self.mazeMap[frontRowIdx][frontColIdx] == 0:
                countWall += 1
            if self.mazeMap[backRowIdx][backColIdx] == 0:
                countWall += 1
            if self.mazeMap[leftRowIdx][leftColIdx] == 0:
                countWall += 1
            if self.mazeMap[rightRowIdx][rightColIdx] == 0:
                countWall += 1
        return countWall


    def calScore(self):
        countWall = self.surroundingWalls()
        if countWall >= 3:
            return -5

    def getPosition(self):
        return self.x, self.y
    
    def getMapPosition(self):
        return int(self.x), int(self.y)
    
    def getAngle(self):
        return self.angle
    
    def draw(self):
        width = self.mazeWidth - self.y
        playerX = self.x * GRIDSIZE + WIDTH / 2 - self.maze.cols * GRIDSIZE / 2
        playerY = self.y * GRIDSIZE + HEIGHT / 2 - self.maze.rows * GRIDSIZE / 2
        drawCircle(playerX, playerY, 5, fill = 'red')
        ## test draw, show the player angle
        # drawLine(playerX, playerY, playerX + width * math.cos(math.radians(self.angle)), 
        #          playerY + width * math.sin(math.radians(self.angle)), fill = 'white')

    