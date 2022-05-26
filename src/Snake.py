import numpy

HEAD = 0
SNAKE_WIDTH = 10


class Snake:

    def __init__(self, start_position_of_head, direction="right"):
        self.head = start_position_of_head  # Tuple co-ordinates
        self.body = []
        self.body_section_directions = []
        self.length = 3
        self.direction = direction
        self.append_into_body_array()

    def get_coordinates_of_body_section(self, body_section_number):
        if body_section_number == HEAD:
            return tuple(self.head)
        else:
            return self.add_up_sections_of_snake(body_section_number - 1,
                                                 tuple(self.head + self.body[body_section_number - 1]))

    # tuple here because numpy makes adding vectors easy but need tuples for comparison

    def add_up_sections_of_snake(self, body_section_number, relative_position):
        if body_section_number == 0:
            return relative_position
        else:
            return (self.add_up_sections_of_snake(body_section_number - 1,
                                                  tuple(relative_position + self.body[body_section_number - 1])))

    def get_length(self):
        return self.length

    def append_into_body_array(self):
        directions: dict[str, tuple[int, int]] = {
            "right": (1, 0),
            "left": (-1, 0),
            "up": (0, 1),
            "down": (0, -1)
        }

        for body_section_from_head in range(1, self.length):
            x_coord_on_grid = -directions[self.direction][0]
            y_coord_on_grid = -directions[self.direction][1]

            x_coord_pixel = x_coord_on_grid * SNAKE_WIDTH
            y_coord_pixel = y_coord_on_grid * SNAKE_WIDTH

            self.body.append(numpy.array([x_coord_pixel, y_coord_pixel]))
            self.body_section_directions.append(self.direction)

    def move_head(self):
        movement_function = {
            "right": lambda: (self.head[0] + SNAKE_WIDTH, self.head[1]),
            "left": lambda: (self.head[0] - SNAKE_WIDTH, self.head[1]),
            "up": lambda: (self.head[0], self.head[1] - SNAKE_WIDTH),
            "down": lambda: (self.head[0], self.head[1] + SNAKE_WIDTH)
        }

        self.head = movement_function[self.direction]()
        self.move_body()

    def move_body(self):
        movement_body_function = {
            "right": lambda: numpy.array([-SNAKE_WIDTH, 0]),
            "left": lambda: numpy.array([SNAKE_WIDTH, 0]),
            "up": lambda: numpy.array([0, SNAKE_WIDTH]),
            "down": lambda: numpy.array([0, -SNAKE_WIDTH])
        }

        for i in range(len(self.body_section_directions) - 1, 0, -1):
            self.body_section_directions[i] = self.body_section_directions[i - 1]

        self.body_section_directions[0] = self.direction

        for i in range(len(self.body)):
            self.body[i] = movement_body_function[self.body_section_directions[i]]()
