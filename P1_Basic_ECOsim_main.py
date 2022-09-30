import pygame
import random
import P1_Basic_ECOsim_class

width = 1366
height = 768
intl_greens = 1
intl_herbivours = 1
intl_carnivours = 1

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption ("ECO Sim")
clock = pygame.time.Clock()

def draw_window():
    game_display.fill ((0, 0, 0))

def main():
    while True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_window()
        clock.tick (60)

if __name__ == '__main__':
    main()
