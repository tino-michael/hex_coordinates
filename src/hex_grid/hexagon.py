from dataclasses import dataclass

from .hex_edge import HexagonEdge
from .hex_vertex import HexagonVertex
from .hex_enums import HexDirection, VertexDirection
from .hex_grid_points import HexGridPoint
from .grid_factory import EdgeFactory, NeighbourFactory, VertexFactory


"""
The slice of the Hexagon's cube coordinates -- i.e. the sum of all three coordinates.
Do not change from 0, otherwise arithmetic (+, -, *) won't work!
"""
SLICE = 0


@dataclass
class Hexagon():

    point: HexGridPoint

    def __init__(self, r, s, t=None):

        if t is None:
            t = SLICE - r - s
        else:
            if r + s + t != SLICE:
                raise ValueError("wrong slice: {r+s+t} != {SLICE}")

        self.point = HexGridPoint(r, s, t)

    def __hash__(self):
        return hash(self.get_rst())

    def get_rst(self):
        return self.point.get_rst()

    def __neg__(self):
        r, s, t = self.get_rst()
        return self.__class__(-r, -s, -t)

    def __add__(self, other):
        r1, s1, t1 = self.get_rst()
        r2, s2, t2 = other.get_rst()

        return self.__class__(r1+r2, s1+s2, t1+t2)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other: int):
        if isinstance(other, int):
            r, s, t = self.get_rst()
            return self.__class__(r*other, s*other, t*other)
        raise TypeError("unsupported operand type")

    def __rmul__(self, other):
        return self.__mul__(other)

    def distance(self, other):
        r1, s1, t1 = self.get_rst()
        r2, s2, t2 = other.get_rst()

        return sum([
            abs(r1 - r2),
            abs(s1 - s2),
            abs(t1 - t2)
        ]) / 2.

    # neighbours
    def neighbour(self, direction: HexDirection) -> "Hexagon":
        point = NeighbourFactory(self.point)(direction)
        return self.__class__(*point.get_rst())

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
        return EdgeFactory(self.point)(direction)

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
        return VertexFactory(self.point)(direction)

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
