import pygame, sys, random
from pygame.locals import *

def draw_rand_line(surface, screen_length, screen_width, max_stroke_width):
    random_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    rand_width = random.randrange(0,5)
    rand_start_pos = random.randrange(0, screen_length), random.randrange(0, screen_width)
    rand_end_pos = random.randrange(0, screen_length), random.randrange(0, screen_width)
    
    pygame.draw.line(surface, random_color, rand_start_pos, rand_end_pos, rand_width)
                

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()

    FPS = 120
    MAX_STROKE_WIDTH = 20 #Maximum thickness of the line
    SCREEN_SIZE = XRES, YRES = 1000, 600
    BG_COLOR = 255,255,255
    
    window = pygame.display.set_mode(SCREEN_SIZE)
    window.fill(BG_COLOR)
    while True:
        draw_rand_line(window, XRES, YRES, MAX_STROKE_WIDTH)
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                    
        pygame.display.flip()       
        fpsClock.tick(FPS)
        
if __name__ == "__main__":
    main()
