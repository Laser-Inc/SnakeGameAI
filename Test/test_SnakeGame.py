import unittest
from src.Grid import Grid


class SnakeGameTest(unittest.TestCase):
    def test_we_have_a_grid(self):
        grid = Grid(10)
        self.assertEqual(150, grid.pixel_width())
        self.assertEqual(150, grid.pixel_height())

    def test_we_have_a_bigger_grid(self):
        grid = Grid(20)
        self.assertEqual(300, grid.pixel_width())
        self.assertEqual(300, grid.pixel_height())
