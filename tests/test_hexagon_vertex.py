from hypothesis import given, assume
from hypothesis.strategies import integers
from .hex_strategies import vertex_directions

from hex_coordinates import (
    Hexagon as H,
    HexagonVertex as V,
)
from hex_coordinates.hex_enums import VertexDirection as VD


@given(integers(), integers(), vertex_directions())
def test_hexagon_vertex(a, b, i):
    assume(i in [VD.top_right, VD.bottom_right])
    assert H(a,b).vertex(i) == V(H(a,b).point, i)
