import math
from cmu_graphics import *
from maze import *
from player import *
import settings

################################################################################
# class RayCasting is for the visulization of 3D maze
# use the raycasting algorithm
# works by casting rays from player's position and checking the intersection
# reference and raycasting tutorial: 
# https://en.wikipedia.org/wiki/Ray_casting#:~:text=Ray%20casting%20is%20the%20most,scenes%20to%20two%2Ddimensional%20images.
# https://www.youtube.com/watch?v=ECqUrT7IdqQ&list=WL&index=2
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
    


    def singleRayCast(self, rayAngle, playerX, playerY):
        # get the grid of the maze, prep for loop to find when ray hit wall
        # can use the worldMap method for Player too
        coorX, coorY = int(playerX), int(playerY)  
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

        ## get the right depth
        if vertDepth <= horiDepth:
            depth = vertDepth
        else:
            depth = horiDepth  

        return depth
    

    def draw2D(self):
        rayAngle = math.radians(self.player.angle) - FOV / 2 + 0.0001
        playerX = self.player.x
        playerY = self.player.y

        for ray in range(RAY_NUM):
            sinA, cosA = math.sin(rayAngle), math.cos(rayAngle)
            depth = self.singleRayCast(rayAngle, playerX, playerY)

            drawLine(playerX * GRIDSIZE + WIDTH / 2 - self.maze.cols * GRIDSIZE / 2,
                    playerY * GRIDSIZE + HEIGHT / 2 - self.maze.rows * GRIDSIZE / 2, 
                    (playerX + depth * cosA) * GRIDSIZE + WIDTH / 2 - self.maze.cols * GRIDSIZE / 2, 
                    (playerY + depth * sinA) * GRIDSIZE + HEIGHT / 2 - self.maze.rows * GRIDSIZE / 2, 
                    lineWidth = 2, fill = 'white') 

            rayAngle += DANGLE


    def draw3D(self):
        rayAngle = math.radians(self.player.angle) - FOV / 2 + 0.0001
        playerX = self.player.x
        playerY = self.player.y
        for ray in range(RAY_NUM):
            
            depth = self.singleRayCast(rayAngle, playerX, playerY)

            #########
            # get projection to visulize in 3D
            depth *= math.cos(math.radians(self.player.angle) - rayAngle) # remove fishbowl effect
            projHeight = abs(SDIST / (depth + 0.0001))

            # draw wall
            gradColor = 250 / (1 + depth ** 6 * 0.0005)
            drawRect(ray * SCALE, HEIGHT // 2 - projHeight // 2, SCALE, projHeight, 
                     fill = rgb(gradColor, gradColor, gradColor))

            rayAngle += DANGLE
