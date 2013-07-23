import pygame, sys, math
import playerclass, wallclass
from pygame.locals import *
from locals import *

pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode(SCREEN_SIZE)

#Player creation
player = playerclass.PlayerClass('Resources/Graphics/statue1.png')
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

def createWall(xPos, yPos):
    #Create a normal wall at said position
    wall = wallclass.WallClass('Resources/Graphics/wall_block.png', xPos, yPos)
    wallGroup.add(wall)
    return wall
def removeWall(xPos, yPos):
    #Remove a normal wall at said position
    for wall in wallGroup:
        if wall.xPos == xPos and wall.yPos == yPos:
            wall.kill()
            wall.rect.x, wall.rect.y = -100,-100
            break
    

    
wallGroup = pygame.sprite.Group()

for i in range(round(XRES / 32)): #32 is wall's width
    for j in range(round(YRES/32)):
        wall = createWall(i, j + 2)
    
for i in range(round(YRES/32)):
    removeWall(5, i)


player.rect.x = 15 * wall.rect.size[0]
player.rect.y = 0 * wall.rect.size[1]


    
while True:
    window.fill(BG_COLOR)
    
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
                player.jump(wallGroup)
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player.move_left = False
            if event.key == K_RIGHT:
                player.move_right = False
            
    pygame.display.flip()
    fpsClock.tick(FPS)

    
