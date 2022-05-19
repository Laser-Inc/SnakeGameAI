import unittest

from SnakeGameAI.src.Snake import Snake
from SnakeGameAI.src.SnakeGame import WIDTH, HEIGHT


class SnakeGameTest(unittest.TestCase):
    def test_check_initial_position_of_snake(self):
        snake = Snake(((WIDTH / 2), (HEIGHT / 2)))
        self.assertEqual(((WIDTH / 2), (HEIGHT / 2)), snake.get_initial_position())

    #def test_check_if_snake_drawn(self):

