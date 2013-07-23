import pygame, sys, math
from pygame.locals import *
from locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self,  xPos, yPos, image):
        pygame.sprite.Sprite.__init__(self) #xPos and yPos is a location system based on a 32x32 grid
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = xPos * 32
        self.rect.y = yPos * 32
        self.move_left = 0
        self.move_right = 0
        self.jump = 0
        self.mspd = 5
        self.hspd = 0   #Horizontal
        self.vspd = 4   #Vertical
        self.jump_height = 10
        self.gravity = 0.1  #Downward acceleration per FRAME
        self.able_move_down = 1
        self.onGround = False
    def update(self, wallGroup):
        self.move(wallGroup)
    
    def move(self, wallGroup):
        """Move while checking for wall collision every pixel"""
        if self.move_left == 1:
            self.hspd = -self.mspd
        elif self.move_right == 1:
            self.hspd = self.mspd
        else:
            self.hspd = 0
            
        if self.onGround == False:
            self.vspd += 0.3
        if self.jump:
            if self.onGround:
                self.vspd -= self.jump_height
        #Move horizontally, then immediately check for horizontal collision
        self.rect.x += self.hspd
        self.check_wall_collide(self.hspd, 0, wallGroup)
        #Move vertically, then immediately check for vertical collision
        self.rect.y += self.vspd
        self.onGround = False
        self.check_wall_collide(0, self.vspd, wallGroup)
    
    def check_wall_collide(self, hspd, vspd, wallGroup):
        """If wall collides, returns True. Otherwise false"""
        for wall in wallGroup:
            if pygame.sprite.collide_rect(self, wall):
                #Moving right when collided
                if hspd > 0:
                    self.rect.right = wall.rect.left
                #Moving left when collided
                if hspd < 0:
                    self.rect.left = wall.rect.right
                #Moving downward/Falling when collided
                if vspd > 0:
                    self.rect.bottom = wall.rect.top
                    self.onGround = True
                    self.vspd = 0
                #Moving upward/Jumping when collided
                if vspd < 0:
                    self.rect.top = wall.rect.bottom
                    self.vspd = 0