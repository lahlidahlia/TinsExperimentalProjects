import pygame, sys, math
from pygame.locals import *
from locals import *

class PlayerClass(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (24,24))
        self.rect = self.image.get_rect()
        self.rect.x = XRES /2
        self.rect.y = YRES /2
        self.hor_speed = 0   #Used for collisions and gravity
        self.ver_speed = 0
        self.max_hor_speed = 8
        self.move_speed = 4
        self.move_left = False
        self.move_right = False
        self.able_move_down = 1 #Determine if player is allowed to move downward
        self.able_move_left = 1
        self.able_move_right = 1
    def update(self, wallGroup):
        #Checking for a wall beneath player's feet and enforce the gravity
        self.move()
        for wall in wallGroup:
            #Checks for a wall 1 px beneath or above player
            if self.check_ver_collision_down(wall):
                self.able_move_down = 0
                break
            else: self.able_move_down = 1
        if self.able_move_down and self.ver_speed <= self.max_hor_speed:
            self.ver_speed += 0.2
        
        #Moving using repeated movement in one fps!
        #Moving up and down
        for i in range(abs(round(self.ver_speed))):
            if self.ver_speed >= 0:
                for wall in wallGroup:
                    if self.check_ver_collision_down(wall):#Checks for a wall 1 px beneath or above player
                        self.able_move_down = 0
                        self.ver_speed = 0
                        break
                else:
                    self.able_move_down = 1
            if self.ver_speed < 0:
                for wall in wallGroup:
                    if self.check_ver_collision_up(wall):#Checks for a wall 1 px beneath or above player
                        self.able_move_down = 0
                        self.ver_speed = 0
                        break
                    else:
                        self.able_move_down = 1
            if self.able_move_down:
                self.rect.y += math.copysign(1, self.ver_speed)

        #Moving left and right
        for i in range(abs(self.hor_speed)):
            if self.move_left == True:
                for wall in wallGroup:  #Checking all the walls for collision
                    if self.check_hor_collision_left(wall):
                        self.able_move_left = 0
                        break
                else:
                    self.able_move_left = 1
                if self.able_move_left:
                    self.rect.x += math.copysign(1, self.hor_speed)
            elif self.move_right == True:
                for wall in wallGroup:
                    if self.check_hor_collision_right(wall):    
                        self.able_move_right = 0
                        break
                else:
                    self.able_move_right = 1
                if self.able_move_right:
                    self.rect.x += math.copysign(1, self.hor_speed)

    def move(self):
        if self.move_left == True:
            self.hor_speed = -self.move_speed
        elif self.move_right == True:
            self.hor_speed = self.move_speed
        else:
            self.hor_speed = 0

    #Functions for easy collision checking(For checking if a wall is 1 px away)
    def check_hor_collision_left(self, wall):
        if self.rect.left - 1 == wall.rect.right and self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.top:
            return True
        else: return False
    def check_hor_collision_right(self, wall):
        if self.rect.right + 1 == wall.rect.left and self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.top:
            return True
        else: return False    
    def check_ver_collision_down(self, wall):
        if self.rect.bottom + 1 == wall.rect.top and self.rect.left - 1 < wall.rect.right and self.rect.right + 1 > wall.rect.left:
            return True
        else: return False
    def check_ver_collision_up(self, wall):
        if self.rect.top + 1 == wall.rect.bottom and self.rect.left - 1 < wall.rect.right and self.rect.right + 1 > wall.rect.left:
            return True
        else: return False
    
    def alarm(self, t):
        #Used to time things in milliseconds
        #When called check if current time is higher than t(= pygame.time.get_ticks() + countdown time in ms)
        if pygame.time.get_ticks() > t:
            return True
        else: return False
    
    def jump(self, wallGroup):
        for wall in wallGroup:
            if self.check_ver_collision_down(wall):
                self.ver_speed = -5
    
    