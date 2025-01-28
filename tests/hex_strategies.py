from hypothesis.strategies import integers, sampled_from, composite

from hex_grid import Hexagon as H
from hex_grid.hex_enums import HexDirection as HD, VertexDirection as VD


@composite
def hex_directions(draw):
    d = draw(sampled_from([HD.right, HD.left, HD.top_right, HD.bottom_right, HD.top_left, HD.bottom_left]))
    return d


@composite
def vertex_directions(draw):
    d = draw(sampled_from([VD.top, VD.top_left, VD.top_right, VD.bottom, VD.bottom_left, VD.bottom_right]))
    return d


@composite
def hexagons(draw):
    h = H(draw(integers(min_value=-20, max_value=20)), draw(integers(min_value=-20, max_value=20)))
    return h
