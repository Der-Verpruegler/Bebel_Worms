import config
import numpy as np
np.random.seed(299)

class Worm():
    def __init__(self):
        self.width = config.WORM_WIDTH
        self.height = config.WORM_HEIGHT
        
        self.corner_col, self.corner_row = self.spawn()

    def spawn(self):
        """ Find a random valid spawn point on map """
        # Valid spawn
        valid_pos = False
        while valid_pos == False:
            # A random column on map
            guess = np.random.randint(1, config.RENDERAREAWIDTH-self.width)
            # Get hitbox coords
            hitbox = self.get_hitbox(col=guess, row=0)
            # Check if there is collision with map in shitbox
            # If not => valid spawn, otherwise try different rand
            if self.check_box_collision(hitbox)==False:
                valid_pos = True
                # Instance vars describing the pos
                corner_col = guess
                corner_row = 0
            
        # Respect gravity
        valid_pos = False
        while valid_pos == False:
            # Get hitbox for current pos lowered by 1 px
            hitbox = self.get_hitbox(col=corner_col, row=corner_row+1)
            # If collision, keep old data as final spawn
            if self.check_box_collision(hitbox)==True:
                valid_pos = True
            # If no collision, bring worm down by 1 px
            else:
                corner_row +=1                
              
        return corner_col, corner_row


    def get_hitbox(self, col, row):
        """ Get worm hitbox, which is a rectangle """
        p1 = [col, row] # upper left
        p2 = [col + self.width, row + self.height] # lower right
        return [p1, p2]
    
    
    def check_box_collision(self, box):
        """ Checks if hitbox touches solid pixel"""
        collision = False
        # efficient boxing
        sub_map = map.solidity[box[0][0]:box[1][0], box[0][1]:box[1][1]]       
        if sub_map.any():
            collision = True           
        
        return collision

      
    def move(self, direction):
        if direction=="left":
            hitbox = self.get_hitbox(col=self.corner_col-1, row=self.corner_row)
            if self.check_box_collision(hitbox) == False:
                self.corner_col -= 1
        elif direction=="right":
            hitbox = self.get_hitbox(col=self.corner_col+1, row=self.corner_row)
            if self.check_box_collision(hitbox) == False:
                self.corner_col += 1
        