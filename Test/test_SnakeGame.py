import unittest
from src.Snake import Snake, HEAD
from src.SnakeGame import WIDTH, HEIGHT, screen, draw_snake, SNAKE_WIDTH

GREEN = (0, 255, 0)


class SnakeGameTest(unittest.TestCase):
    def test_check_initial_position_of_snake(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")
        self.assertEqual(centre_screen, snake.get_coordinates_of_body_section(HEAD))

    def test_check_if_snake_drawn(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")
        draw_snake(snake)
        self.assertEqual(GREEN, screen.get_at(snake.get_coordinates_of_body_section(HEAD)))

    def test_check_multiple_positions_of_snake(self):
        centre_screen = (WIDTH // 2, HEIGHT // 2)

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")
        draw_snake(snake)
        for i in range(snake.get_length()):
            self.assertEqual(GREEN, screen.get_at(snake.get_coordinates_of_body_section(i)))

    # ToDo: Have snake body sections (and maybe direction) initialised inside snake class. TICK
    # ToDo: Abstract snake body sections to be relative to head position. TICK

    def test_snake_initially_facing_right(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, SNAKE_WIDTH, "right")

        for body_section in range(snake.get_length()):
            self.assertEqual((centre_screen[0] - body_section * SNAKE_WIDTH, centre_screen[1]),
                             snake.get_coordinates_of_body_section(body_section))

    def test_snake_initially_facing_left(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, SNAKE_WIDTH, "left")

        for body_section in range(snake.get_length()):
            self.assertEqual((centre_screen[0] + body_section * SNAKE_WIDTH, centre_screen[1]),
                             snake.get_coordinates_of_body_section(body_section))
