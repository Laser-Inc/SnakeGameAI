import numpy


class Snake:
    def __init__(self, start_position_of_head, body_width):
        self.head = start_position_of_head  # Tuple co-ordinates
        self.body = [numpy.array([-1 * body_width, 0]),  # Body positions relative to head
                     numpy.array([-2 * body_width, 0])]
        self.length = 1 + len(self.body)
        self.body_width = body_width

    def get_coords_of_body_section(self, body_section_number):
        if body_section_number == 0:
            return self.head
        else:

            return self.head + self.body[body_section_number - 1]

    def get_length(self):
        return self.length


HEAD = 0
