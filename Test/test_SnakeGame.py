import unittest
import pygame

from SnakeGameAI.src.Snake import Snake
from SnakeGameAI.src.SnakeGame import WIDTH, HEIGHT, screen, draw_snake


class SnakeGameTest(unittest.TestCase):
    def test_check_initial_position_of_snake(self):
        snake = Snake(((WIDTH / 2), (HEIGHT / 2)))
        self.assertEqual(((WIDTH / 2), (HEIGHT / 2)), snake.get_initial_position())

    def test_check_if_snake_drawn(self):
        snake = Snake((int((WIDTH / 2)), int((HEIGHT / 2))))
        GREEN = (0, 255, 0)
        draw_snake()
        print(screen.get_at(snake.get_initial_position()))
        self.assertEqual(GREEN, screen.get_at(snake.get_initial_position()))
