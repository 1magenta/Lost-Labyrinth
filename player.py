from cmu_graphics import *
import random
import math
from settings import *
################################################################################
# class player is for defining the player's position, movement
################################################################################

class Player:
    level = 0
    def __init__(self, maze):
        self.maze = maze
        #initilize player defaut position, maze.entrance only store the index of row and col
        (self.y, self.x) = maze.entrance
        self.x += 0.5
        self.y += 0.5
        self.mazeMap = maze.maze
        self.mazeWidth = GRIDSIZE * maze.cols
        self.angle = initAngle
        self.step = 0.5
        self.legalMove = True
        self.Win = False 


    # def goRight(self): #call this method by keyboard input
    #     sign = 1
    #     newX = self.y + sign*self.step
    #     newY = self.x
    #     if not self.collision:
    #         self.y, self.x = newX, newY
    
    # def goLeft(self): #call this method by keyboard input
    #     sign = -1
    #     newX = self.y + sign*self.step
    #     newY = self.x
    #     if not self.collision:
    #         self.y, self.x = newX, newY
    
    # def goDown(self): #call this method by keyboard input
    #     sign = -1
    #     newY = self.x + sign*self.step
    #     newX = self.y
    #     if not self.collision:
    #         self.y, self.x = newX, newY

    # def goUp(self): #call this method by keyboard input
    #     sign = 1
    #     newX = self.y + sign*self.step
    #     newY = self.x
    #     if not self.collision:
    #         self.y, self.x = newX, newY            

    #3D version control 
    #use keyboard to control player's movement, up down arrow to move
    #right and left to change the player's direction

    def move(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        dx, dy = 0, 0
        speed = playerSpeed * dTime
        sinSpeed = speed * sinA
        cosSpeed = speed * cosA


    def moveForward(self): #call this method by keyboard input         
        print(self.x, self.y)
        print(1, self.legalMove)                
        newX = self.x + self.step * math.cos(math.radians(self.angle))
        newY = self.y + self.step * math.sin(math.radians(self.angle))
        self.checkCollision(newX, newY)
        # print(2, self.legalMove) 
        if self.legalMove:
            self.x, self.y = newX, newY


    def moveBackward(self): #call this method by keyboard input
        print(self.x, self.y)
        print(1, self.legalMove)                         
        newX = self.x - self.step * math.cos(math.radians(self.angle))
        newY = self.y - self.step * math.sin(math.radians(self.angle))
        self.checkCollision(newX, newY)
        # print(2, self.legalMove)  
        if self.legalMove:
            self.x, self.y = newX, newY


    def turnRight(self):
        self.angle -= 15

    def turnLeft(self):
        self.angle += 15
            
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
        (exitX, exitY) = self.maze.exit
        if self.y >= exitX and self.x >= exitY:
            self.win = True
            level += 1

    
    def Score(self):
        pass

       
    
    def getPosition(self):
        return self.y, self.x
    
    def getMapPosition(self):
        return int(self.y), int(self.x)
    
    def getAngle(self):
        return self.angle
    
    def draw(self):
        width = self.mazeWidth - self.y
        playerX = self.x * GRIDSIZE
        playerY = self.y * GRIDSIZE
        # drawCircle(self.x * GRIDSIZE + GRIDSIZE/2, self.y * GRIDSIZE + GRIDSIZE/2, 5, fill = 'red')
        drawCircle(playerX, playerY, 5, fill = 'red')
        drawLine(playerX, playerY, playerX + width * math.cos(math.radians(self.angle)), 
                 playerY + width * math.sin(math.radians(self.angle)), fill = 'yellow')

        # drawLine(self.x * GRIDSIZE + GRIDSIZE/2, self.y * GRIDSIZE + GRIDSIZE/2, 
        #          self.x * GRIDSIZE + width * math.cos(math.radians(self.angle)), 
        #          self.y * GRIDSIZE + GRIDSIZE/2 + width * math.sin(math.radians(self.angle)),
        #          lineWidth = 2)
    