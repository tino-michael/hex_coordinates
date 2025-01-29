from dataclasses import dataclass

from .hex_grid_points import HexGridPoint
from .hex_enums import HexDirection

from .hex_grid_directions import get_neighbour_step


@dataclass
class HexagonEdge():
    point: HexGridPoint

    def __init__(self, hex: HexGridPoint, dir: HexDirection):
        # the edge of a hexagon is just half the distance to the corresponding neighbour
        r1, s1, t1 = hex.get_rst()
        r2, s2, t2 = get_neighbour_step(dir).get_rst()
        self.point = HexGridPoint(r1+r2/2., s1+s2/2., t1+t2/2., offgrid=True)

    def __hash__(self):
        return hash("HexGridPoint") + hash(self.point.get_rst())
