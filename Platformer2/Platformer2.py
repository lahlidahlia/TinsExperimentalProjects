import pygame, sys
import playerClass, wallClass
from pygame.locals import *
from locals import *



def createWall(xPos, yPos):
    wall = wallClass.Wall(xPos, yPos, "Resources/Graphics/wall_block.png")
    wallGroup.add(wall)
    return wall

    
def createPlayer(xPos, yPos):
    player = playerClass.Player(xPos, yPos, 'Resources/Graphics/statue1.png')
    playerGroup.add(player)
    return player




pygame.init()   
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode(SCREEN_SIZE)



playerGroup = pygame.sprite.Group()
wallGroup = pygame.sprite.Group()

room = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W       P          W",
    "W                  W",
    "W W W W W W W W W WW",
    "WW W W W W W W W W W",
    "WWWWWWWWWWWWWWWWWWWW",
]
for row, i in zip(room, range(len(room))):    #X value
    for col, j in zip(row, range(len(row))): #Y value
        if col == "W":
            wall = createWall(j, i)
        if col == "P":
            player = createPlayer(j, i)

#Main loop
while True:
    window.fill(WINDOW_COLOR)
    playerGroup.draw(window)
    wallGroup.draw(window)
    
    player.update(wallGroup)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
            if event.key == K_LEFT:
                player.move_left = True
                player.move_right = False
            if event.key == K_RIGHT:
                player.move_right = True
                player.move_left = False
            if event.key == K_UP:
                player.jump = 1
            
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player.move_left = False
            if event.key == K_RIGHT:
                player.move_right = False
            if event.key == K_UP:
                player.jump = 0
                
    pygame.display.flip()
    fpsClock.tick(FPS)
