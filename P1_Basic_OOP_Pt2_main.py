import pygame
import random
from P1_Basic_OOP_Pt1_class import Blob

width = 800
height = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

starting_green_blobs = 50
starting_blue_blobs = 15
starting_red_blobs = 5

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

def draw_environment(green_blobs, blue_blobs, red_blobs):
    game_display.fill (BLACK)
    for blob_id in green_blobs:
        Blob = green_blobs[blob_id]
        pygame.draw.circle (game_display, Blob.colour, [Blob.x_cord, Blob.y_cord], Blob.size)
        Blob.move()
    for blob_id in blue_blobs:
        Blob = blue_blobs[blob_id]
        pygame.draw.circle (game_display, Blob.colour, [Blob.x_cord, Blob.y_cord], Blob.size)
        Blob.move()
    for blob_id in red_blobs:
        Blob = red_blobs[blob_id]
        pygame.draw.circle (game_display, Blob.colour, [Blob.x_cord, Blob.y_cord], Blob.size)
        Blob.move()
    pygame.display.update()

def main():
    green_blobs = dict(enumerate([Blob(GREEN, 1, 800, 600, 0) for i in range(starting_green_blobs)]))
    blue_blobs = dict(enumerate([Blob(BLUE, 3, 800, 600, 1) for i in range(starting_blue_blobs)]))
    red_blobs = dict(enumerate([Blob(RED, 5, 800, 600, 2) for i in range(starting_red_blobs)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw_environment (green_blobs, blue_blobs, red_blobs)
        clock.tick (120)

if __name__ == '__main__':
    main()