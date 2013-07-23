import pygame, sys, random
import room_gen
from pygame.locals import *
from locals import *

pygame.init()
fpsClock = pygame.time.Clock()
      
Room = room_gen.Room_Gen()

window = pygame.display.set_mode(SCREEN_SIZE)

wallGroup = pygame.sprite.Group()

while True:
    window.fill(BG_COLOR)
    
    Room.wallGroup.draw(window)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    pygame.display.flip()