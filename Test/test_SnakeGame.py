import unittest

import numpy

from src.Snake import Snake, HEAD
from src.SnakeGame import WIDTH, HEIGHT, screen, draw_snake, SNAKE_WIDTH

GREEN = (0, 255, 0)


class SnakeGameTest(unittest.TestCase):
    def test_check_initial_position_of_snake(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")
        self.assertEqual(centre_screen, snake.get_coords_of_body_section(HEAD))

    def test_check_if_snake_drawn(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")
        draw_snake(snake)
        self.assertEqual(GREEN, screen.get_at(snake.get_coords_of_body_section(HEAD)))

    def test_check_multiple_positions_of_snake(self):
        centre_screen = (WIDTH // 2, HEIGHT // 2)

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")
        draw_snake(snake)
        for i in range(snake.get_length()):
            self.assertEqual(GREEN, screen.get_at(snake.get_coords_of_body_section(i)))

# ToDo: Have snake body sections (and maybe direction) initialised inside snake class. TICK
# ToDo: Abstract snake body sections to be relative to head position. TICK

    def test_snake_initially_facing_right(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))
        one_right_of_centre_screen = (WIDTH // 2 - 1 * SNAKE_WIDTH, HEIGHT // 2)  # Body positions relative to head
        two_right_of_centre_screen = (WIDTH // 2 - 2 * SNAKE_WIDTH, HEIGHT // 2)  # Body positions relative to head

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")

        self.assertEqual(centre_screen, snake.get_coords_of_body_section(HEAD))
        self.assertEqual(one_right_of_centre_screen, snake.get_coords_of_body_section(1))
        self.assertEqual(two_right_of_centre_screen, snake.get_coords_of_body_section(2))

    def test_snake_initially_facing_left(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))
        one_left_of_centre_screen = (WIDTH // 2 + 1 * SNAKE_WIDTH, HEIGHT // 2)  # Body positions relative to head
        two_left_of_centre_screen = (WIDTH // 2 + 2 * SNAKE_WIDTH, HEIGHT // 2)  # Body positions relative to head

        snake = Snake(centre_screen, SNAKE_WIDTH, "left")

        self.assertEqual(centre_screen, snake.get_coords_of_body_section(HEAD))
        self.assertEqual(one_left_of_centre_screen, snake.get_coords_of_body_section(1))
        self.assertEqual(two_left_of_centre_screen, snake.get_coords_of_body_section(2))


