from typing import Dict, Tuple

import numpy


class Snake:

    def __init__(self, start_position_of_head, body_width, direction="right"):
        self.head = start_position_of_head  # Tuple co-ordinates
        self.body = []
        self.length = 3
        self.body_width = body_width
        self.direction = direction

        self.append_into_body_array()

    def get_coordinates_of_body_section(self, body_section_number):
        if body_section_number == 0:
            return tuple(self.head)
        else:
            return tuple(self.head + self.body[body_section_number - 1])

    # tuple here because numpy makes adding vectors easy but need tuples for comparison

    def get_length(self):
        return self.length

    def append_into_body_array(self):
        direction_dict: dict[str, tuple[int, int]] = {
            "right": (1, 0),
            "left": (-1, 0)
        }

        for multiplier in range(1, self.length):
            self.body.append(
                numpy.array([-direction_dict[self.direction][0] * self.body_width * multiplier,
                             direction_dict[self.direction][1]]))


HEAD = 0
