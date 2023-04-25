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

    def rayCast(self):
        rayAngle = math.radians(self.player.angle) - FOV / 2 + 0.0001

        playerX = self.player.x
        playerY = self.player.y
        # get the grid of the maze, prep for loop to find when ray hit wall
        # can use the worldMap method for Player too
        coorX, coorY = int(playerX), int(playerY)

        for ray in range(RAY_NUM):
            sinA, cosA = math.sin(rayAngle), math.cos(rayAngle)
            
            # intersect with vertical grids
            # get intersect point postion: vertX, vertY
            if cosA > 0:
                vertX = coorX + 1
                dX = 1
            else:
                # if cosA < 0, coorX should substract a small number in order to check the left cell 
                vertX = coorX - 1e-6
                dX = -1
            vertDepth = (vertX - playerX) / cosA
            vertY = vertDepth * sinA + playerY

            dDepth = dX / cosA
            dY = dDepth * sinA

            # check if the the ray hits wall, if not extend the ray to check
            for i in range(MAX_DEPTH):
                rowIdx, colIdx = int(vertY), int(vertX)
                grid = self.maze.maze
                if grid[rowIdx][colIdx] == 0:
                    break
                vertX += dX
                vertY += dY
                vertDepth += dDepth
                # i += 1
            

            # intersect with horizontal grids
            # get intersect point postion: horiX, horiY
            if sinA > 0:
                horiY = coorY + 1
                dY = 1
            else:
                # if cosA < 0, coorX should substract a small number in order to check the left cell 
                horiY = coorY - 1e-6
                dX = -1
            horiDepth = (horiY - playerY) / sinA
            horiX = horiDepth * sinA + playerX

            dDepth = dY / sinA
            dX = dDepth * cosA

            # check if the the ray hits wall, if not extend the ray to check
            for d in range(MAX_DEPTH):
                rowIdx, colIdx = int(vertY), int(vertX)
                print(rowIdx, colIdx)
                print(grid[rowIdx][colIdx])
                grid = self.maze.maze
                if grid[rowIdx][colIdx] == 0:
                    break
                horiX += dX
                horiY += dY
                vertDepth += dDepth
                # i += 1  

            if vertDepth < horiDepth:
                depth = vertDepth
            else:
                depth = horiDepth         

            # test to draw
            drawLine(playerX, playerY, playerX + depth * cosA, playerY + depth * sinA, lineWidth = 2, fill = 'yellow') 

            rayAngle += DANGLE



        
        
        
        
        
        
        
        
        
        # self.rayCastRes = []
        
        # posiX, posiY = self.game.player.getPosition() #should define a player class and getPosition method
        # mapX, mapY = self.game.player.getMapPosition()

        
        # raysNum = 50
        # #calculate initial ray angle
        # halfFOV = math.radians(60) / 2
        # rayAngle = np.linspace(self.game.player.angle - halfFOV + 0.0001,
        #                      self.game.player.angle + halfFOV, num = raysNum)
        # sinA = np.sin(rayAngle)
        # cosA = np.cos(rayAngle)

        # #loop through wach ray, and calculate sin and cos
        # #then caluculate intersections with walls
       
        # #horizontal
        # horiY, dY = np.where(sinA > 0, (mapY + 1, 1), (mapY - 1e-6, -1))
        # horiDepth = (horiY - posiX) / sinA
        # horiX = posiX + horiDepth * cosA

        # deltaDepth = dY / sinA
        # dX = deltaDepth * cosA

        # horiTexture = np.full(raysNum, 1)
        # maxDepth = 30
        # for i in range(maxDepth):
        #     horiX += dX
        #     horiY += dY
        #     horiDepth += deltaDepth
        #     horiTile = np.array(list(zip(horiX.astype(int), horiY.astype(int))))
        #     for idX, tile in enumerate(horiTile):
        #         if tuple(tile) in _: #get a world map here
        #             horiTexture[idX] = _
        
        # #vertical
        # vertX, dX = np.where(cosA > 0, (mapX + 1, 1), (mapX - 1e-6, -1))
        # vertDepth = (vertX - posiX) / cosA
        # vertY = posiY + vertDepth * sinA

        # deltaDepth = dX / cosA
        # dY = deltaDepth * sinA

        # vertTexture = np.full(raysNum, 1)
        # for i in range(maxDepth):
        #     vertX += dX
        #     vertY += dY
        #     vertDepth += deltaDepth
        #     vertTile = np.array(list(zip(vertX.astype(int), vertY.astype(int))))
        #     for idX, tile in enumerate(vertTile):
        #         if tuple(tile) in _: #get a world map here
        #             horiTexture[idX] = _
        
        # #determine the depth and texture offset for each ray intersection
        # if vertDepth < horiDepth:
        #     depth = vertDepth
        #     texture = vertTexture
        #     vertY %= 1
        #     if cosA > 0:   
        #         offset = vertY
        #     else:
        #         offset = 1 - vertY
        # else:
        #     depth = horiDepth
        #     texture = horiTexture
        #     horiX %= 1
        #     if sinA > 0:   
        #         offset = 1 - horiX
        #     else:
        #         offset = horiX
        # #remove fishbowl effect by multiplying the depth by the cosine of the 
        # #difference between the player's angle and the ray angle
        # depth *= math.cos(self.game.player.angle - rayAngle)
        # #calculate projection height based on the corrected depth
        # projHeight = _

        # self.rayCastRes = list(zip(depth, projHeight, texture, offset))
        


