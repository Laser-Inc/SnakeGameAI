import unittest
import pygame

from src.Snake import Snake
from src.SnakeGame import WIDTH, HEIGHT, screen, draw_snake, CELL_WIDTH, CELL_HEIGHT

GREEN = (0, 255, 0)


class SnakeGameTest(unittest.TestCase):
    def test_check_initial_position_of_snake(self):
        snake = Snake([((WIDTH / 2), (HEIGHT / 2))])
        self.assertEqual(((WIDTH / 2), (HEIGHT / 2)), snake.get_current_position()[0])

    def test_check_if_snake_drawn(self):
        snake = Snake([(int((WIDTH / 2)), int((HEIGHT / 2)))])
        draw_snake(snake)
        print(screen.get_at(snake.get_current_position()[0]))
        self.assertEqual(GREEN, screen.get_at(snake.get_current_position()[0]))

    def test_check_multiple_positions_of_snake(self):
        snake = Snake([(WIDTH // 2, HEIGHT // 2), (WIDTH // 2 - CELL_WIDTH, HEIGHT // 2 - CELL_HEIGHT), (WIDTH // 2 - CELL_WIDTH * 2, HEIGHT // 2 - CELL_HEIGHT * 2)])
        draw_snake(snake)
        for i in range(len(snake.get_current_position())):
            self.assertEqual(GREEN, screen.get_at(snake.get_current_position()[i]))