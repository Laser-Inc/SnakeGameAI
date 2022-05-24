import sys

import pygame

from src.Snake import Snake

pygame.init()

WIDTH = 500
HEIGHT = 500
SNAKE_WIDTH = 10
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

centre_screen = (WIDTH // 2, HEIGHT // 2)
snake = Snake(centre_screen, SNAKE_WIDTH, "right")


def main():
    draw_snake(snake)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def draw_snake(snake_to_draw):
    for i in range(snake_to_draw.get_length()):
        pygame.draw.rect(screen, GREEN,
                         pygame.Rect(snake_to_draw.get_coords_of_body_section(i)[0],
                                     snake_to_draw.get_coords_of_body_section(i)[1],
                                     SNAKE_WIDTH, SNAKE_WIDTH))
    pygame.display.flip()


if __name__ == '__main__':
    main()
