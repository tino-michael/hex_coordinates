from dataclasses import dataclass
from .hex_edge import HexagonEdge
from .hex_vertex import HexagonVertex
from .hex_enums import HexDirection, VertexDirection
from .hex_grid_points import HexGridPoint
from .hex_grid_directions import get_neighbour_step


"""
The slice of the Hexagon's cube coordinates -- i.e. the sum of all three coordinates.
Do not change from 0, otherwise arithmetic (+, -, *) won't work!
"""
SLICE = 0


@dataclass
class Hexagon():
    point: HexGridPoint

    def __hash__(self):
        return hash(self.get_rst())

    def get_rst(self):
        return self.point.get_rst()

    def __add__(self, other: "Hexagon"):
        if isinstance(other, Hexagon):
            return self.__class__(self.point + other.point)
        elif isinstance(other, HexGridPoint):
            return self.__class__(self.point + other)
        raise TypeError

    def __sub__(self, other: "Hexagon"):
        if isinstance(other, Hexagon):
            return self.__class__(self.point - other.point)
        elif isinstance(other, HexGridPoint):
            return self.__class__(self.point - other)
        raise TypeError

    def __mul__(self, other: int):
        if isinstance(other, int):
            return self.__class__(self.point * other)
        raise TypeError("unsupported operand type")

    def __rmul__(self, other: int):
        return self.__mul__(other)

    def distance(self, other: "Hexagon"):
        if isinstance(other, Hexagon):
            return self.point.distance(other.point)
        raise TypeError

    # neighbours
    def neighbour(self, direction: HexDirection) -> "Hexagon":
        step = get_neighbour_step(direction)
        return self.__class__(self.point + step)

    def right(self):
        return self.neighbour(HexDirection.right)

    def top_right(self):
        return self.neighbour(HexDirection.top_right)

    def bottom_right(self):
        return self.neighbour(HexDirection.bottom_right)

    def left(self):
        return self.neighbour(HexDirection.left)

    def top_left(self):
        return self.neighbour(HexDirection.top_left)

    def bottom_left(self):
        return self.neighbour(HexDirection.bottom_left)

    # edges
    def edge(self, direction: HexDirection) -> HexagonEdge:
        return HexagonEdge(self.point, direction)

    def right_edge(self):
        return self.edge(HexDirection.right)

    def top_right_edge(self):
        return self.edge(HexDirection.top_right)

    def bottom_right_edge(self):
        return self.edge(HexDirection.bottom_right)

    def left_edge(self):
        return self.edge(HexDirection.left)

    def top_left_edge(self):
        return self.edge(HexDirection.top_left)

    def bottom_left_edge(self):
        return self.edge(HexDirection.bottom_left)

    # vertices
    def vertex(self, direction: VertexDirection) -> HexagonVertex:
        return HexagonVertex(self.point, direction)

    def top_vertex(self):
        return self.vertex(VertexDirection.top)

    def top_left_vertex(self):
        return self.vertex(VertexDirection.top_left)

    def top_right_vertex(self):
        return self.vertex(VertexDirection.top_right)

    def bottom_vertex(self):
        return self.vertex(VertexDirection.bottom)

    def bottom_left_vertex(self):
        return self.vertex(VertexDirection.bottom_left)

    def bottom_right_vertex(self):
        return self.vertex(VertexDirection.bottom_right)
