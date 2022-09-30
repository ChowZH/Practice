import random

class Blob:
    def __init__ (self, colour, sizerange, x_bound, y_bound, movespeed, growscore = 1): #initialise blobs, takes colour, avg size, window boundary, and movespeed and returns with a blob to fulfill the properties)
        self.colour = colour
        self.size = random.randrange(sizerange, sizerange + 2)
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.x_cord = random.randrange(0, self.x_bound)
        self.y_cord = random.randrange(0, self.y_bound)
        self.movespeed = movespeed
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

    def grow(self, colour):
        pass
    
    def dtct_clsn(self, target_id):        
        pass