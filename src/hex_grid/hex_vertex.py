from dataclasses import dataclass

from .hex_grid_points import HexGridPoint
from .hex_enums import VertexDirection, HexDirection

from .hex_grid_directions import get_neighbour_step


@dataclass
class HexagonVertex():
    point: HexGridPoint

    def __init__(self, hex: HexGridPoint, dir: VertexDirection):

        # In a 3D cube grid, the vertices are half a cell-width away from the center in every direction.
        # So, the GridPoint step is +- 1/2 in every coordinate, depending on the specific vertex.
        # E.g, for a pointy-top hexagon, the top vertex direction is half-way between the
        # directions of the top-left and top-right neighbours.
        # So, to get the step to the top vertex, add the directions to the two adjacent
        # hex-neighbours (to get the +- of the coordinates) and scale each to 1/2.
        def get_vertex_step(d1: VertexDirection, d2: VertexDirection):
            r, s, t = (get_neighbour_step(d1) + get_neighbour_step(d2)).get_rst()
            return HexGridPoint(r/abs(2*r), s/abs(2*s), t/abs(2*t), offgrid=True)

        match dir:
            case VertexDirection.top:
                step = get_vertex_step(
                    HexDirection.top_left, HexDirection.top_right)

            case VertexDirection.bottom:
                step = get_vertex_step(
                    HexDirection.bottom_left, HexDirection.bottom_right)

            case VertexDirection.top_right:
                step = get_vertex_step(
                    HexDirection.right, HexDirection.top_right)

            case VertexDirection.bottom_right:
                step = get_vertex_step(
                    HexDirection.right, HexDirection.bottom_right)

            case VertexDirection.top_left:
                step = get_vertex_step(
                    HexDirection.left, HexDirection.top_left)

            case VertexDirection.bottom_left:
                step = get_vertex_step(
                    HexDirection.left, HexDirection.bottom_left)
            case _:
                raise TypeError

        self.point = hex + step
