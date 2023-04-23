from cmu_graphics import *
import random
import math
################################################################################
# class player is for defining the player's position, movement
################################################################################

class Player:
    def __init__(self, position, maze):
        self.x, self.y = position
        self.maze = maze
        self.angle = 90
        self.step = 1
    
    def goRight(self): #call this method by keyboard input
        sign = 1
        newX = self.x + sign*self.step
        newY = self.y
        if not self.checkCollision(newX, newY):
            self.x, self.y = newX, newY
    
    def goLeft(self): #call this method by keyboard input
        sign = -1
        newX = self.x + sign*self.step
        newY = self.y
        if not self.checkCollision(newX, newY):
            self.x, self.y = newX, newY
    
    def goDown(self): #call this method by keyboard input
        sign = -1
        newY = self.y + sign*self.step
        newX = self.x
        if not self.checkCollision(newX, newY):
            self.x, self.y = newX, newY

    def goUp(self): #call this method by keyboard input
        sign = 1
        newX = self.x + sign*self.step
        newY = self.y
        if not self.checkCollision(newX, newY):
            self.x, self.y = newX, newY            

    #3D version control 
    #use keyboard to control player's movement, up down arrow to move
    #right and left to change the player's direction
    def moveForward(self): #call this method by keyboard input
        newX = self.x + self.step * math.cos(math.radians(self.angle))
        newY = self.y + self.step * math.sin(math.radians(self.angle))
        if not self.checkCollision(newX, newY):
            self.x, self.y = newX, newY
    def moveBackward(self): #call this method by keyboard input
        newX = self.x - self.step * math.cos(math.radians(self.angle))
        newY = self.y - self.step * math.sin(math.radians(self.angle))
        if not self.checkCollision(newX, newY):
            self.x, self.y = newX, newY

    def turnRight(self):
        self.angle -= 10

    def turnLeft(self):
        self.angle += 10
    
    def checkCollosion(self, x, y):
       return not self.maze.isWall
    
    def getPosition(self):
        return self.x, self.y
    
    def getAngle(self):
        return self.angle
    
    def draw(self):
        drawCircle(self.x, self.y, 5, fill = 'red')
    