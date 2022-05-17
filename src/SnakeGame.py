import sys

import pygame

from src.Grid import Grid

grid = Grid(50)
pygame.init()
screen = pygame.display.set_mode((grid.pixel_width(), grid.pixel_height()))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
