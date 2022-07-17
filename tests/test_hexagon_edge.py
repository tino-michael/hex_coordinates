from hypothesis import given
from hypothesis.strategies import integers, sampled_from

from hex_coordinates import (
    Hexagon as H,
    HexagonEdge as E,
    HexDirection as HD
)


@given(integers(), integers(), sampled_from([HD.right, HD.top_right, HD.bottom_right]))
def test_hexagon_edge(a, b, i):
    assert H(a,b).edge(i) == E(H(a,b).point, i)

@given(integers(), integers(),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_edge_neighbour(a, b, d):

    c = ""
    if "right" in d:
        c = d.replace("right", "left")
    elif "left" in d:
        c = d.replace("left", "right")

    if "bottom" in d:
        c = c.replace("bottom", "top")
    elif "top" in d:
        c = c.replace("top", "bottom")

    assert H(a, b).edge(HD[d]) == H(a, b).neighbour(HD[d]).edge(HD[c])
