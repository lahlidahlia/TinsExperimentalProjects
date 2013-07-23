import pygame, sys
from pygame.locals import *
from locals import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = xPos * 32, yPos * 32
    
    
