import pygame, sys
from pygame.locals import *
from locals import *

class Walls(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
        self.rect = self.image.get_rect()
        self.xPos = xPos
        self.yPos = yPos
        self.rect.x = self.xPos * GRID_SIZE
        self.rect.y = self.yPos * GRID_SIZE
    
