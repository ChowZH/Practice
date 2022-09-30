import random

class Organism:
    def __init__ (self, spawn_x_bound, spawn_y_bound, category):
        self.category = category
        self.spawn_x_bound = spawn_x_bound
        self.spawn_y_bound = spawn_y_bound
        if category == prod:
            self.colour = (0, 255, 0)
            self.size = randrange(1, 2)
        elif category == herb:
            self.colour = (0, 0, 255)
            self.size = randrange(5, 6)
        elif category == carn:
            self.colour = (255, 0, 0)
            self.size = randrange(7, 8)

    def grow ():
        pass