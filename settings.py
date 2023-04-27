import math

################################################################################
# game settings
# include constants used in the project
################################################################################

WIDTH, HEIGHT = 1050, 750
GRIDSIZE = 50

dTime = 1
initAngle = 90
playerSpeed = 0.1

# for rayCasting
FOV = math.pi / 3
# FOV = 60
RAY_NUM = WIDTH // 2
HALF_RAYS = RAY_NUM // 2
DANGLE = FOV / RAY_NUM
MAX_DEPTH = 100
SDIST = WIDTH // 2 / math.tan(FOV / 2)
SCALE = WIDTH // RAY_NUM


DELTA = 0.05
STRIP_WIDTH = 5

MAX_LEVELS = 5

