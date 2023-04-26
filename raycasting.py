import math
from cmu_graphics import *
import numpy as np
from maze import *
from player import *
import settings

################################################################################
# class RayCasting is for rendering 3D scenes
# it works by casting rays from player's position and checking the intersection
# reference: 
# https://github.com/StanislavPetrovV/DOOM-style-Game/blob/main/raycasting.py
################################################################################

class RayCasting:
    def __init__(self, maze, player):
        # self.game = game
        self.maze = maze
        self.player = player
        self.rayCastRes = []
        self.obj = []
    
    def renderObject(self):
        pass

    def isValidIndex(self, row, col):
        return 0 <= row < len(self.maze.maze) and 0 <= col < len(self.maze.maze[0])

    def rayCast(self):
        rayAngle = math.radians(self.player.angle) - FOV / 2 + 0.0001

        playerX = self.player.x
        playerY = self.player.y
        # get the grid of the maze, prep for loop to find when ray hit wall
        # can use the worldMap method for Player too
        coorX, coorY = int(playerX), int(playerY)

        for ray in range(RAY_NUM):
            sinA, cosA = math.sin(rayAngle), math.cos(rayAngle)
            
            #########
            # intersect with vertical grids
            # get intersect point postion: vertX, vertY
            if cosA > 0:
                vertX = coorX + 1
                dX1 = 1
            else:
                # if cosA < 0, coorX should substract a small number in order to check the left cell 
                vertX = coorX - 1e-6
                dX1 = -1
            vertDepth = (vertX - playerX) / cosA
            vertY = vertDepth * sinA + playerY

            dDepth1 = dX1 / cosA
            dY1 = dDepth1 * sinA

            #########
            # check if the the ray hits wall, if not extend the ray to check
            for i in range(MAX_DEPTH):
                rowIdx, colIdx = int(vertY), int(vertX)
                grid = self.maze.maze
                if self.isValidIndex(rowIdx, colIdx) and grid[rowIdx][colIdx] == 0:
                    break
                vertX += dX1
                vertY += dY1
                vertDepth += dDepth1
                # i += 1
            
            #########
            # intersect with horizontal grids
            # get intersect point postion: horiX, horiY
            if sinA > 0:
                horiY = coorY + 1
                dY2 = 1
            else:
                horiY = coorY - 1e-6
                dY2 = -1
            horiDepth = (horiY - playerY) / sinA
            horiX = horiDepth * cosA + playerX

            dDepth2 = dY2 / sinA
            dX2 = dDepth2 * cosA

            #########
            # check if the the ray hits wall, if not extend the ray to check
            for j in range(MAX_DEPTH):
                rowIdx, colIdx = int(horiY), int(horiX)
                # print(rowIdx, colIdx)
                # print(grid[rowIdx][colIdx])
                grid = self.maze.maze
                if self.isValidIndex(rowIdx, colIdx) and grid[rowIdx][colIdx] == 0:
                    break
                horiX += dX2
                horiY += dY2
                horiDepth += dDepth2
                # i += 1  

            ## get the right depth, and remove the fishbowl effect   
            if vertDepth <= horiDepth:
                depth = vertDepth
            else:
                depth = horiDepth  
            depth *= math.cos(math.radians(self.player.angle) - rayAngle) 

            # test to draw, it is a 2D version 
            # drawLine(playerX * GRIDSIZE, playerY * GRIDSIZE, 
            #          (playerX + depth * cosA) * GRIDSIZE, 
            #          (playerY + depth * sinA) * GRIDSIZE, lineWidth = 2) 
            
            #########
            # get projection to visulize in 3D
            projHeight = SDIST / (depth + 0.0001)

            # draw wall
            gradColor = 250 / (1 + depth ** 6 * 0.0005)
            drawRect(ray * SCALE, HEIGHT // 2 - projHeight // 2, SCALE, projHeight, 
                     fill = rgb(gradColor, gradColor, gradColor))

            rayAngle += DANGLE
