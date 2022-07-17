from enum import Enum, auto

class HexDirection(Enum):
    right = auto()
    left = auto()
    top_right = auto()
    bottom_right = auto()
    top_left = auto()
    bottom_left = auto()

class VertexDirection(Enum):
    top = auto()
    bottom = auto()
    top_right = auto()
    bottom_right = auto()
    top_left = auto()
    bottom_left = auto()
