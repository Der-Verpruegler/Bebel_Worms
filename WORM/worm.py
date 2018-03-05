import config
import numpy as np

class Worm():
    def __init__(self):
        self.width = config.WORM_WIDTH
        self.height = config.WORM_HEIGHT
        self.spawn()


    def spawn(self):
        """ Find a random valid spawn point on map """
        # Valid spawn
        valid_pos = False
        while valid_pos == False:
            # A random column on map
            guess = np.random.randint(0, config.RENDERAREAWIDTH-self.width)
            # Get hitbox coords
            hitbox = self.get_hitbox(col=guess, row=0)
            # Check if there is collision with map in shitbox
            # If not => valid spawn, otherwise try different rand
            if not self.check_for_box_collision(hitbox):
                valid_pos = True
                # Instance vars describing the pos
                self.corner_col = guess
                self.corner_row = 0

        # Respect gravity
        valid_pos = False
        while valid_pos == False:
            # Get hitbox for current pos lowered by 1 px
            hitbox = self.get_hitbox(col=self.corner_col, row=self.corner_row+1)
            # If collision, keep old data as final spawn
            if self.check_for_box_collision(hitbox):
                valid_pos = True
            # If no collision, bring worm down by 1 px
            else:
                self.corner_row +=1

        return self.corner_col, self.corner_row


    def get_hitbox(self, col, row):
        """ Get worm hitbox, which is a rectangle """
        p1 = [col, row] # upper left
        p2 = [col + self.width, row + self.height] # lower right
        return [p1, p2]
    
    
    def check_for_box_collision(self, box):
        """ Checks if hitbox touches solid pixel"""
        # Throw exception message if out of map, should be avoided
        if box[0][0] < 0: or 
            raise Exception("Out of Map, box[0][0]:" + str(box[0][0]))
        if box[1][0] > config.RENDERAREAWIDTH:
            raise Exception("Out of Map, box[1][0]:" + str(box[1][0]))
            
        # efficient boxing        
        sub_map = map.solidity[box[0][0]:box[1][0], box[0][1]:box[1][1]]       
        return sub_map.any()


    def move(self, direction):
        if direction=="left":
            # Catch border of map
            if not self.corner_col-1 > 0:                
                hitbox = self.get_hitbox(col=self.corner_col-1, row=self.corner_row)
                if not self.check_for_box_collision(hitbox):
                    self.corner_col -= 1

        elif direction=="right":
            # Catch border of map
            if not self.corner_col+1 > (config.RENDERAREAWIDTH-config.WORM_WIDTH):
                # If move is permitted
                hitbox = self.get_hitbox(col=self.corner_col+1, row=self.corner_row)
                if not self.check_for_box_collision(hitbox):
                    self.corner_col += 1
