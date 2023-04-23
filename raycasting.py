import math
from cmu_graphics import *
import numpy as np
from maze import *
from player import *

################################################################################
# class RayCasting is for rendering 3D scenes
# it works by casting rays from player's position and checking the intersection
# reference: 
# https://github.com/StanislavPetrovV/DOOM-style-Game/blob/main/raycasting.py
################################################################################

class RayCasting:
    def __init__(self, game):
        self.game = game
        self.rayCastRes = []
        self.obj = []
    
    def renderObject(self):
        pass

    def rayCast(self):
        self.rayCastRes = []
        
        posiX, posiY = self.game.player.getPosition() #should define a player class and getPosition method
        mapX, mapY = self.game.player.getMapPosition()

        
        raysNum = 50
        #calculate initial ray angle
        halfFOV = math.radians(60) / 2
        rayAngle = np.linspace(self.game.player.angle - halfFOV + 0.0001,
                             self.game.player.angle + halfFOV, num = raysNum)
        sinA = np.sin(rayAngle)
        cosA = np.cos(rayAngle)

        #loop through wach ray, and calculate sin and cos
        #then caluculate intersections with walls
       
        #horizontal
        horiY, dY = np.where(sinA > 0, (mapY + 1, 1), (mapY - 1e-6, -1))
        horiDepth = (horiY - posiX) / sinA
        horiX = posiX + horiDepth * cosA

        deltaDepth = dY / sinA
        dX = deltaDepth * cosA

        horiTexture = np.full(raysNum, 1)
        maxDepth = 30
        for i in range(maxDepth):
            horiX += dX
            horiY += dY
            horiDepth += deltaDepth
            horiTile = np.array(list(zip(horiX.astype(int), horiY.astype(int))))
            for idx, tile in enumerate(horiTile):
                if tuple(tile) in _: #get a world map here
                    horiTexture[idx] = _
        
        #vertical
        vertX, dX = np.where(cosA > 0, (mapX + 1, 1), (mapX - 1e-6, -1))
        vertDepth = (vertX - posiX) / cosA
        vertY = posiY + vertDepth * sinA

        deltaDepth = dX / cosA
        dY = deltaDepth * sinA

        vertTexture = np.full(raysNum, 1)
        for i in range(maxDepth):
            vertX += dX
            vertY += dY
            vertDepth += deltaDepth
            vertTile = np.array(list(zip(vertX.astype(int), vertY.astype(int))))
            for idx, tile in enumerate(vertTile):
                if tuple(tile) in _: #get a world map here
                    horiTexture[idx] = _
        
        #determine the depth and texture offset for each ray intersection
        if vertDepth < horiDepth:
            depth = vertDepth
            texture = vertTexture
            vertY %= 1
            if cosA > 0:   
                offset = vertY
            else:
                offset = 1 - vertY
        else:
            depth = horiDepth
            texture = horiTexture
            horiX %= 1
            if sinA > 0:   
                offset = 1 - horiX
            else:
                offset = horiX
        #remove fishbowl effect by multiplying the depth by the cosine of the 
        #difference between the player's angle and the ray angle
        depth *= math.cos(self.game.player.angle - rayAngle)
        #calculate projection height based on the corrected depth
        projHeight = _

        self.rayCastRes = list(zip(depth, projHeight, texture, offset))
        


