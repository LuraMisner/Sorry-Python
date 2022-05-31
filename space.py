from enum import Enum


class reserved_type(Enum):
    NONE = 'None'
    START = 'Start'
    HOME = 'Home'
    RED_SLIDE = 'Red Slide'
    YELLOW_SLIDE = 'Yellow Slide'
    GREEN_SLIDE = 'Green Slide'
    BLUE_SLIDE = 'Blue Slide'
    RED_SAFETY = 'Red Safety'
    YELLOW_SAFETY = 'Yellow Safety'
    GREEN_SAFETY = 'Green Safety'
    BLUE_SAFETY = 'Blue Safety'


class occupied_type(Enum):
    NONE = 'None'
    GREEN = 'Green'
    BLUE = 'Blue'
    RED = 'Red'
    YELLOW = 'Yellow'


class Space:
    def __init__(self):
        self.occupied = occupied_type.NONE
        self.type = reserved_type.NONE

    def get_occupied(self):
        return self.occupied

    def set_occupied(self, change):
        self.occupied = change

    def get_type(self):
        return self.type

    def set_type(self, enum):
        self.type = enum

    def to_string(self):
        return str(self.occupied) + ', ' + str(self.type)

    def board_string(self):
        if self.occupied == occupied_type.GREEN:
            return "[G]"
        elif self.occupied == occupied_type.BLUE:
            return "[B]"
        elif self.occupied == occupied_type.RED:
            return "[R]"
        elif self.occupied == occupied_type.YELLOW:
            return "[Y]"
        elif self.type == reserved_type.START:
            return "[%]"
        elif self.type == reserved_type.HOME:
            return "[H]"
        elif self.type == reserved_type.RED_SLIDE or self.type == reserved_type.BLUE_SLIDE or \
                self.type == reserved_type.GREEN_SLIDE or self.type == reserved_type.YELLOW_SLIDE:
            return "[~]"
        elif self.type == reserved_type.BLUE_SAFETY or self.type == reserved_type.RED_SAFETY or \
                self.type == reserved_type.GREEN_SAFETY or self.type == reserved_type.YELLOW_SAFETY:
            return "[#]"
        else:
            return "[ ]"
