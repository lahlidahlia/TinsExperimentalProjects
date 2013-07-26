import pygame, sys, random, time, math
import walls
from pygame.locals import *
from locals import *

class Room_Gen(object):
    def __init__(self):
        self.t = time.time()
        self.room_pos = {}
        self.wallGroup = pygame.sprite.Group()
        
        self.start_room_pos = round(MAX_XPOS/2) - 10, round(MAX_YPOS/2) - 10
        
        #Used to generate random length and width room
        self.min_room_length = 5
        self.max_room_length = 15
        self.min_room_width = 5
        self.max_room_width = 15
        
        #Used to generate random length tunnel, width isn't necessary yet since tunnel width is always 1 for now
        self.tunnel_length_min = 2  
        self.tunnel_length_max = 10
        
        self.room_skipped = 0 #Used in order to avoid keyerror checking for room numbers in dictionary, also doubled as a variable
                              #to check how many rooms were skipped
        
        self.last_dir = 0
        self.build_level()
        print("Room coordinates: {}".format(self.room_pos))
        print("Room skipped: {}".format(self.room_skipped))
        print("Time elapsed: {:.2f} seconds".format(time.time() - self.t))

    def build_level(self):
        """Randomly builds the whole level!"""
        self.fill_level()
        self.create_rect_room(self.start_room_pos[0], self.start_room_pos[1], self.rand_room_len(), self.rand_room_wid())
        for i in range(1, AMOUNT_OF_ROOMS):
            if self.build_another_room(i - self.room_skipped):
                pass
            else: self.room_skipped += 1
    
    def build_another_room(self, room_number):
        """Build another room out of the given room number. Will check whether room location is applicable, if so return True, otherwise False"""
        direction = self.rand_dir()
        while direction == self.last_dir:
            direction = self.rand_dir()
        tun_len = self.rand_tun_len()
        room_len, room_wid = self.rand_room_len(), self.rand_room_wid()
        if self.check_applicable_room(room_number, direction, tun_len, room_len, room_wid):
            self.build_tun_and_room(room_number, direction, tun_len, room_len, room_wid)
            self.last_dir = self.get_opposite_last_dir(direction)

            print(direction)
            return True
        else: return False
    
    def build_tun_and_room(self, room_number, direction, tun_len, room_len, room_wid):
        tunnel_end = self.tunnel_given_direction(room_number, direction, tun_len)
        if direction == "E":
            self.create_room_east(tunnel_end, room_len, room_wid)
        if direction == "W":
            self.create_room_west(tunnel_end, room_len, room_wid)
        if direction == "N":
            self.create_room_north(tunnel_end, room_len, room_wid)
        if direction == "S":
            self.create_room_south(tunnel_end, room_len, room_wid)
    
    def create_wall(self, xPos, yPos):
        """Creates a wall at position (xPos, yPos) on a grid system"""
        self.wall = walls.Walls(xPos, yPos, "Graphics/wall_block.png")
        self.wallGroup.add(self.wall)

    def delete_wall(self, xPos, yPos):
        """It checks for a wall with the given position and deletes it (doesn't do anything if theres no wall in that pos)"""
        for wall in self.wallGroup:
            if wall.xPos == xPos and wall.yPos == yPos:
                self.wallGroup.remove(wall)
                break

    def fill_level(self):
        """Fill the whole room with walls"""
        for x in range(MAX_XPOS):
            for y in range(MAX_YPOS):
                self.create_wall(x, y)

    def rand_dir(self):
        """Chooses a random direction to tunnel a room"""
        directions = ["E", "W", "N", "S"]
        return random.choice(directions)
    
    def get_opposite_last_dir(self, direction):
        if direction == "E":
            return "W"
        if direction == "W":
            return "E"
        if direction == "N":
            return "S"
        if direction == "S":
            return "N"
    
    
    def check_applicable_room(self, room_number, direction, tun_len, room_len, room_wid):
        applicable = 1
        room_info = self.room_pos[str(room_number)]
        if direction == "E":
            tunnel_start = (room_info[2], random.randrange(room_info[1], room_info[3]))
            tunnel_end = tunnel_start[0] + tun_len, tunnel_start[1]
            if tunnel_end[0] + room_len > MAX_XPOS - ROOM_OFFSET:
                applicable = 0
            elif tunnel_end[1] - room_wid < ROOM_OFFSET or tunnel_end[1] + room_wid > MAX_YPOS - ROOM_OFFSET:
                applicable = 0
        if direction == "W":
            tunnel_start = (room_info[0] - tun_len, random.randrange(room_info[1], room_info[3]))
            tunnel_end = tunnel_start[0], tunnel_start[1]
            if tunnel_end[0] - room_len < ROOM_OFFSET:
                applicable = 0
            elif tunnel_end[1] - room_wid < ROOM_OFFSET or tunnel_end[1] + room_wid > MAX_YPOS - ROOM_OFFSET:
                applicable = 0
        if direction == "N":
            tunnel_start = (random.randrange(room_info[0], room_info[2]), room_info[1] - tun_len)
            tunnel_end = tunnel_start[0], tunnel_start[1]
            if tunnel_end[1] - room_wid < ROOM_OFFSET:
                applicable = 0
            elif tunnel_end[0] - room_len < ROOM_OFFSET or tunnel_end[0] + room_wid > MAX_XPOS - ROOM_OFFSET:
                applicable = 0
        if direction == "S":
            tunnel_start = (random.randrange(room_info[0], room_info[2]), room_info[3])
            tunnel_end = tunnel_start[0], tunnel_start[1] + tun_len
            if tunnel_end[1] + room_wid > MAX_YPOS - ROOM_OFFSET:
                applicable = 0
            elif tunnel_end[0] - room_len < ROOM_OFFSET or tunnel_end[0] + room_wid > MAX_XPOS - ROOM_OFFSET:
                applicable = 0
        
        if applicable == 1:
            return True
        else: return False
    
    """Room creating functions"""
    def create_rect_room(self, xstart, ystart, length, width):
        """Form a room by deleting walls"""
        for x in range(xstart, length + xstart):
            for y in range(ystart, width + ystart):
                self.delete_wall(x, y)
        self.record_room_info(xstart, ystart, xstart + length, ystart + width)
        
    def rand_room_len(self):
        room_length = random.randrange(self.min_room_length + 1, self.max_room_length + 1)
        return room_length
    
    def rand_room_wid(self):
        room_width = random.randrange(self.min_room_width + 1,self.max_room_width + 1)
        return room_width
    
    def record_room_info(self, xPos1, yPos1, xPos2, yPos2):
        """Record the room position in (x1, y1, x2, y2) format to a dictionary with a room_number as a key"""
        for i in range(1, 1000):
            if not(str(i) in self.room_pos):
                self.room_pos[str(i)] = (xPos1, yPos1, xPos2, yPos2)
                room_number = i
                break
        print("{} : {}".format(room_number, self.room_pos[str(room_number)]))
    
    def create_room_east(self, tunnel_end, room_length, room_width):
        room_start = tunnel_end[0], tunnel_end[1] - (room_width - random.randrange(1, room_width + 1))
        self.create_rect_room(room_start[0], room_start[1], room_length, room_width)
    
    def create_room_west(self, tunnel_end, room_length, room_width):
        room_start = tunnel_end[0] - room_length, tunnel_end[1] - (room_width - random.randrange(1, room_width + 1))
        self.create_rect_room(room_start[0], room_start[1], room_length, room_width)
        
    def create_room_north(self, tunnel_end, room_length, room_width):
        room_start = tunnel_end[0] - (room_length - random.randrange(1, room_length + 1)), tunnel_end[1] - room_width
        self.create_rect_room(room_start[0], room_start[1], room_length, room_width)
        
    def create_room_south(self, tunnel_end, room_length, room_width):
        room_start = tunnel_end[0] - (room_length - random.randrange(1, room_length + 1)), tunnel_end[1]
        self.create_rect_room(room_start[0], room_start[1], room_length, room_width)
    
    

    """Tunneling functions, all return the position of the end of the tunnel"""
    def create_tunnel(self, xstart, ystart, length, width):
        """Base function, create a tunnel, switch the length and width for vertical tunnel."""
        for x in range(xstart, length + xstart):
            for y in range(ystart, width + ystart):
                self.delete_wall(x, y)
    
    def rand_tun_len(self): 
        return random.randrange(self.tunnel_length_min + 1, self.tunnel_length_max + 1)
    
    def tunnel_given_direction(self, room_key, direction, length):
        """Tunnels a tunnel in a given direction, returns the end of the tunnel. 
           Tunnel length is specified up on the class __init__"""
        if direction == "N":
            tunnel_end = self.tunnel_north(room_key, length, 1)
        if direction == "S":
            tunnel_end = self.tunnel_south(room_key, length, 1)
        if direction == "W":
            tunnel_end = self.tunnel_west(room_key, length, 1)
        if direction == "E":
            tunnel_end = self.tunnel_east(room_key, length, 1)
        return tunnel_end
    
    def tunnel_east(self, room_number, length, width):
        """Tunnel East"""
        room_info = self.room_pos[str(room_number)]
        tunnel_start = (room_info[2], random.randrange(room_info[1], room_info[3]))
        self.create_tunnel(tunnel_start[0], tunnel_start[1], length, width)
        tunnel_end = tunnel_start[0] + length, tunnel_start[1]
        #self.draw_tun_arrow("E", tunnel_start, length, tunnel_end)
        return tunnel_end
        
    def tunnel_west(self, room_number, length, width):
        """Tunnel West"""
        room_info = self.room_pos[str(room_number)]
        tunnel_start = (room_info[0] - length, random.randrange(room_info[1], room_info[3]))
        self.create_tunnel(tunnel_start[0], tunnel_start[1], length, width)
        tunnel_end = tunnel_start[0], tunnel_start[1]
        return tunnel_end
    
    def tunnel_north(self, room_number, length, width):
        """Tunnel North"""
        room_info = self.room_pos[str(room_number)]
        tunnel_start = (random.randrange(room_info[0], room_info[2]), room_info[1] - length)
        self.create_tunnel(tunnel_start[0], tunnel_start[1], width, length)
        tunnel_end = tunnel_start[0], tunnel_start[1]
        return tunnel_end
            
    def tunnel_south(self, room_number, length, width):
        """Tunnel South"""
        room_info = self.room_pos[str(room_number)]
        tunnel_start = (random.randrange(room_info[0], room_info[2]), room_info[3])
        self.create_tunnel(tunnel_start[0], tunnel_start[1], width, length)
        tunnel_end = tunnel_start[0], tunnel_start[1] + length
        return tunnel_end
    #def draw_tun_arrow(self, direction, tunnel_start, tun_len, tunnel_end):
    #    if direction == "E":
    #        pygame.draw.line(window, (0,0,0), (tunnel_start[0]*GRID_SIZE, tunnel_start[1]*GRID_SIZE + GRID_SIZE/2), (tunnel_end[0]*GRID_SIZE, tunnel_end[1]*GRID_SIZE + GRID_SIZE/2))
    #    if direction == "W":
    #        pass
    #    if direction == "N":
    #        pass
    #    if direction == "S":
    #        pass
    #