import pygame, sys
from pygame.locals import *
from locals import *

class WallClass(pygame.sprite.Sprite):
    def __init__(self, image, xPos, yPos): #xPos and yPos will determine wall's location in a grid-like fashion
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.xPos = xPos
        self.yPos = yPos
        self.rect.x = self.xPos * self.rect.size[0]
        self.rect.y = self.yPos * self.rect.size[1]
