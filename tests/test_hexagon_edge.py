from hypothesis import given
from hypothesis.strategies import sampled_from

from .hex_strategies import hexagons, hex_directions

from hex_grid import (
    HexDirection as HD,
    HexagonEdge as E
)


@given(hexagons(), hex_directions())
def test_hexagon_edge(h, d):
    assert h.edge(d) == E(h.point, d)


@given(
    hexagons(),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_edge_neighbour(h, d):

    c = ""
    if "right" in d:
        c = d.replace("right", "left")
    elif "left" in d:
        c = d.replace("left", "right")

    if "bottom" in d:
        c = c.replace("bottom", "top")
    elif "top" in d:
        c = c.replace("top", "bottom")

    assert h.edge(HD[d]) == h.neighbour(HD[d]).edge(HD[c])


@given(
    hexagons(),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_edge_distant(h, d):

    assert h.edge(HD[d]) != h.neighbour(HD[d]).edge(HD[d])
