from dataclasses import dataclass

from .hex_grid_points import HexGridPoint
from .hex_enums import VertexDirection


@dataclass
class HexagonVertex():
    hex : HexGridPoint
    dir : VertexDirection
