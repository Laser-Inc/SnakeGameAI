class Grid:
    PIXELS_PER_CELL = 15

    def __init__(self, size):
        self.size = size

    def pixel_width(self):
        return self.size * self.PIXELS_PER_CELL

    def pixel_height(self):
        return self.pixel_width()
