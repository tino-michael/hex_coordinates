import pytest
from hypothesis import given
from hypothesis.strategies import integers, floats, sampled_from
from .hex_strategies import hexagons

from hex_coordinates import (
    Hexagon as H,
    HexDirection as HD,
)

from hex_coordinates.hexagon import SLICE
from hex_coordinates.grid_factory import get_neighbour_step


@given(integers(), integers())
def test_hexagon(a, b):
    assert H(a, b) == H(a, b, SLICE-a-b)


@given(integers(), integers(), integers(), integers())
def test_hexagon_subtraction(a, b, x, y):
    assert H(a, b) - H(x, y) == H(a-x, b-y)


@given(integers(), integers(), integers())
def test_hexagon_multiplication_integer(a, b, c):
    assert H(a, b) * c == H(a*c, b*c)
    assert a * H(b, c) == H(a*b, a*c)

@given(integers(), integers(), integers(), integers())
def test_hexagon_multiplication_hexagon(a, b, x, y):
    with pytest.raises(TypeError):
        H(a, b) * H(x, y)

@given(integers(), integers(), floats())
def test_hexagon_multiplication_float(a, b, c):
    with pytest.raises(TypeError):
        H(a, b) * c

@given(hexagons(), integers(min_value=1, max_value=6))
def test_hexagon_direction_by_int(h, i):
    assert h.neighbour(HD(i)) == h + get_neighbour_step(HD(i))

@given(hexagons(),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_direction_by_str(h, d):
        assert getattr(h, d)() == h + get_neighbour_step(HD[d])
        assert getattr(h, d)() == h.neighbour(HD[d])
