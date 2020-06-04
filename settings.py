import math

# game settings

WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS_POS = (WIDTH - 65, 5)
FPS = 60
TILE = 100

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE//MAP_SCALE
MAP_POS = (0, HEIGHT-HEIGHT//MAP_SCALE)

# players settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2


# ray-castings settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * TILE
SCALE = WIDTH // NUM_RAYS

# colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0,)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
YELLOW = (220,220,0)
