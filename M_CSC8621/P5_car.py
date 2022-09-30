# Task 1
class Car:
    def __init__ (self, year, make):
        self.year = year
        self.make = make
        self.speed = 0

    def accelerate (self):
        self.speed += 5

    def brake (self):
        self.speed -= 5

    def get_speed (self):
        return print (self.speed)