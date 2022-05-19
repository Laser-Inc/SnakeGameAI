import sys

import pygame

from SnakeGameAI.src.Snake import Snake

pygame.init()

WIDTH = 500
HEIGHT = 500
CELL_WIDTH = 10
CELL_HEIGHT = 10
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
snake = Snake(((WIDTH / 2), (HEIGHT / 2)))


def main():
    draw_snake()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def draw_snake():
    pygame.draw.rect(screen, GREEN,
                     pygame.Rect(snake.get_initial_position()[0], snake.get_initial_position()[1], CELL_WIDTH,
                                 CELL_HEIGHT))
    pygame.display.flip()


if __name__ == '__main__':
    main()
