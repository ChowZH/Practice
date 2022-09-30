import pygame
import random
from P2_foodchain_class import Organism as Org

# Window settings and colour definitions
width = 800
height = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Assingment 2")
clock = pygame.time.Clock()

# Initial organism number settings
starting_prod = 100
Starting_herb = 50
starting_carn = 3



# Draw frame function, including updating each frame
def draw_eco(prods, herbs, carns):
    game_display.fill (BLACK)
    # For each organism in prods, herbs, carns dictionary, update position in display
    to_purge = []
    for org_id_prod in prods:
        Org = prods[org_id_prod]
        pygame.draw.circle (game_display, Org.colour, [Org.x_cord, Org.y_cord], Org.size)
        Org.move()
        # Detect collision between current producer and all herbivores
        for org_id_herb in herbs:
            if Org.detect_collision(herbs[org_id_herb]) == True:
                to_purge.append(org_id_prod)

    for purge in to_purge:
        prods.pop(purge)
    to_purge.clear

    to_purge = []
    for org_id_herb in herbs:
        Org = herbs[org_id_herb]
        pygame.draw.circle (game_display, Org.colour, [Org.x_cord, Org.y_cord], Org.size)
        Org.move()
        # Detect collision between current herbivores and all carnivores
        for org_id_carn in carns:
            if Org.detect_collision(carns[org_id_carn]) == True:
                to_purge.append(org_id_herb)
        # detect collision, if collide with prod, add to growth value
        # if growth value reach threshold, create new herb
        # if growth value stagnant after time, die 

    for purge in to_purge:
        herbs.pop(purge)
    to_purge.clear

    for org_id in carns:
        Org = carns[org_id]
        pygame.draw.circle (game_display, Org.colour, [Org.x_cord, Org.y_cord], Org.size)
        Org.move()
        # detect collision, if collide with herb, add to growth value
        # if growth value reach threshold, create new carn
        # if growth value stagnant after time, die
    # Update display
    pygame.display.update()

def main():
    # Producers: green, size range 1, boundaries at 800:600, movespeed 0. Growth not yet implemented
    prods = dict(enumerate([Org(GREEN, 1, 800, 600, 0, 0) for i in range(starting_prod)]))
    # Producers: green, size range 3, boundaries at 800:600, movespeed 1. Growth not yet implemented
    herbs = dict(enumerate([Org(BLUE, 3, 800, 600, 1, 1) for i in range(Starting_herb)]))
    # Producers: green, size range 5, boundaries at 800:600, movespeed 2. Growth not yet implemented
    carns = dict(enumerate([Org(RED, 5, 800, 600, 2, 2) for i in range(starting_carn)]))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        draw_eco(prods, herbs, carns)
        clock.tick (120)

if __name__ == '__main__':
    main()