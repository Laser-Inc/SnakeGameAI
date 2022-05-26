import unittest
from src.Snake import Snake, HEAD, SNAKE_WIDTH
from src.SnakeGame import WIDTH, HEIGHT, screen, draw_snake

GREEN = (0, 255, 0)


class SnakeGameTest(unittest.TestCase):
    def test_check_initial_position_of_snake(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "right")
        self.assertEqual(centre_screen, snake.get_coordinates_of_body_section(HEAD))

    def test_check_if_snake_drawn(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "right")
        draw_snake(snake)
        self.assertEqual(GREEN, screen.get_at(snake.get_coordinates_of_body_section(HEAD)))

    def test_check_multiple_positions_of_snake(self):
        centre_screen = (WIDTH // 2, HEIGHT // 2)

        snake = Snake(centre_screen, "right")
        draw_snake(snake)
        for i in range(snake.get_length()):
            self.assertEqual(GREEN, screen.get_at(snake.get_coordinates_of_body_section(i)))

    # ToDo: Have snake body sections (and maybe direction) initialised inside snake class. TICK
    # ToDo: Abstract snake body sections to be relative to head position. TICK

    def test_snake_initially_facing_right(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "right")

        for body_section in range(snake.get_length()):
            self.assertEqual((centre_screen[0] - body_section * SNAKE_WIDTH, centre_screen[1]),
                             snake.get_coordinates_of_body_section(body_section))

    def test_snake_initially_facing_left(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "left")

        for body_section in range(snake.get_length()):
            self.assertEqual((centre_screen[0] + body_section * SNAKE_WIDTH, centre_screen[1]),
                             snake.get_coordinates_of_body_section(body_section))

    def test_snake_initially_facing_up(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "up")

        for body_section in range(snake.get_length()):
            self.assertEqual((centre_screen[0], centre_screen[1] - body_section * SNAKE_WIDTH),
                             snake.get_coordinates_of_body_section(body_section))

    def test_snake_initially_facing_down(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "down")

        for body_section in range(snake.get_length()):
            self.assertEqual((centre_screen[0], centre_screen[1] + body_section * SNAKE_WIDTH),
                             snake.get_coordinates_of_body_section(body_section))

    def test_the_snake_head_moves_right(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "right")
        snake.move_head()

        self.assertEqual((centre_screen[0] + SNAKE_WIDTH, centre_screen[1]),
                         snake.get_coordinates_of_body_section(HEAD))

    def test_the_snake_body_follows_the_head_right(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "right")
        snake.move_head()

        self.assertEqual(centre_screen, snake.get_coordinates_of_body_section(1))

    def test_the_snake_head_moves_up(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "up")
        snake.move_head()

        self.assertEqual((centre_screen[0], centre_screen[1] - SNAKE_WIDTH),
                         snake.get_coordinates_of_body_section(HEAD))

    def test_the_snake_head_moves_left(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "left")
        snake.move_head()

        self.assertEqual((centre_screen[0] - SNAKE_WIDTH, centre_screen[1]),
                         snake.get_coordinates_of_body_section(HEAD))

    def test_the_snake_head_moves_down(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "down")
        snake.move_head()

        self.assertEqual((centre_screen[0], centre_screen[1] + SNAKE_WIDTH),
                         snake.get_coordinates_of_body_section(HEAD))

    def test_the_snake_turns_left(self):
        centre_screen = ((WIDTH // 2), (HEIGHT // 2))

        snake = Snake(centre_screen, "right")
        snake.direction = "up"
        snake.move_head()

        self.assertEqual(centre_screen, snake.get_coordinates_of_body_section(1))


