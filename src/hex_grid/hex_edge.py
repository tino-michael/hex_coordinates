from dataclasses import dataclass

from .hex_grid_points import HexGridPoint
from .hex_enums import HexDirection


@dataclass
class HexagonEdge():
    hex : HexGridPoint
    dir : HexDirection

    def __hash__(self):
        return hash((hex, dir))
