import random
import math

class Organism:
    # Initialize organism type, takes in colour, size range, ecosystem boundary, average movespeed, and growth score
    # All values initialized in main()
    def __init__(self, colour, sizerange, x_bound, y_bound, movespeed, chainlevel, growscore = 1):
        self.colour = colour
        self.size = random.randrange(sizerange, sizerange + 2)
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.x_cord = random.randrange(0, self.x_bound)
        self.y_cord = random.randrange(0, self.y_bound)
        self.movespeed = movespeed
        self.chainlevel = chainlevel
        self.growscore = growscore

    def move(self):
        self.move_x = random.randrange(-1, 2)*self.movespeed
        self.move_y = random.randrange(-1, 2)*self.movespeed
        if self.move_x == 0:
            self.x_cord = self.x_cord
        elif self.move_y == 0:
            self.y_cord = self.y_cord
        self.x_cord += self.move_x
        self.y_cord += self.move_y

        if self.x_cord < 0:
            self.x_cord = 0
        elif self.x_cord > self.x_bound:
            self.x_cord = self.x_bound

        if self.y_cord < 0:
            self.y_cord = 0
        elif self.y_cord > self.y_bound:
            self.y_cord = self.y_bound

    def grow(self):
        pass
    
    def detect_collision(self, target_id):        
        x_1 = self.x_cord
        x_2 = target_id.x_cord
        y_1 = self.y_cord
        y_2 = target_id.y_cord
        # Get distance between target center and self canter
        point_distance = math.sqrt((x_1-x_2)*(x_1-x_2) + (y_1-y_2)*(y_1-y_2))
        
        sum_of_size = self.size + target_id.size

        # To be changed to sum of target and self size
        if point_distance > sum_of_size:
            return False
        else:
            return True
