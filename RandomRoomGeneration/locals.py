import math
SCREEN_SIZE = XRES, YRES = 1088, 672
BG_COLOR = 255, 255, 255
GRID_SIZE = 8
MAX_XPOS = math.ceil((XRES / GRID_SIZE))  #Adding the 0.6 in order to always round up the number
MAX_YPOS = math.ceil((YRES / GRID_SIZE))
AMOUNT_OF_ROOMS = 50
ROOM_OFFSET = 3 #the amount tiles that rooms needs to be away from the edge of the level