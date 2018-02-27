import config
import numpy as np


class Worm():
    def __init__(self):
        self.size_x = 5 #temp
        self.size_y = 10 #temp
        self.corner_col, self.corner_row = self.spawn()

    def spawn(self):
        """ Find a random valid spawn point on map """
        # Valid spawn
        valid_pos = False
        while valid_pos == False:
            # A random column on map
            guess = np.random.randint(1, config.RENDERAREAWIDTH-self.size_x)
            # Get hitbox coords
            hitbox = self.get_hitbox(col=guess, row=0)
            # Check if there is collision with map in shitbox
            # If not => valid spawn, otherwise try different rand
            if self.check_for_collision(hitbox)==False:
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
            if self.check_for_collision(hitbox)==True:
                valid_pos = True
            # If no collision, bring worm down by 1 px
            else:
                corner_row +=1
        
        return corner_col, corner_row


    def get_hitbox(self, col, row):
        """ Get worm hitbox """
        p1 = [col, row]
        p2 = [col + self.size_x, row + self.size_y]
        return [p1, p2]
    
    
    def check_for_collision(self, hitbox):
        """ Checks if hitbox touches solid pixel"""
        collision = False
        for col in range(hitbox[0][0], hitbox[1][0]):
            for row in range(hitbox[0][1], hitbox[1][1]):
                if col>config.RENDERAREAWIDTH or col<0 or map.px_get_solidity(col, row)==True:
                    collision = True
                if collision == True:
                    break
            if collision == True:
                break
        return collision

      
    def move(self, direction):
        if direction=="left":
            if self.check_for_collision(self.get_hitbox(col=self.corner_col-1, row=self.corner_row)) == False:
                self.corner_col -= 1
        elif direction=="right":
            if self.check_for_collision(self.get_hitbox(col=self.corner_col+1, row=self.corner_row)) == False:
                self.corner_col += 1

#map = MapBackend()        
#w = Worm()
#w.spawn()
#for i in range(1000):
    #print(w.corner_col, w.corner_row)
    #w.move("right")

        