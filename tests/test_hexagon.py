import pytest
from hypothesis import given
from hypothesis.strategies import integers, floats, sampled_from
from .hex_strategies import hexagons

from hex_grid import (
    Hexagon as H,
    HexDirection as HD,
)

from hex_grid.hexagon import SLICE
from hex_grid.grid_factory import get_neighbour_step


@given(integers(), integers())
def test_hexagon(a, b):
    assert H(a, b) == H(a, b, SLICE-a-b)


@given(integers(), integers(), integers(), integers())
def test_hexagon_addition(a, b, x, y):
    assert H(a, b) + H(x, y) == H(a+x, b+y)


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


@given(
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_neighbour_distance(d):
    h1 = H(0, 0)
    h2 = h1.neighbour(HD[d])

    assert h1.distance(h2) == h2.distance(h1) == 1


@given(hexagons())
def test_opposing(h):
    left = h.left()
    right = h.right()

    top_left = h.top_left()
    bottom_right = h.bottom_right()

    bottom_left = h.bottom_left()
    top_right = h.top_right()

    assert left.distance(right) == 2
    assert bottom_left.distance(top_right) == 2
    assert top_left.distance(bottom_right) == 2


@given(hexagons())
def test_adjacent(h):
    left = h.left()
    right = h.right()

    top_left = h.top_left()
    bottom_right = h.bottom_right()

    bottom_left = h.bottom_left()
    top_right = h.top_right()

    assert left.distance(top_left) == left.distance(bottom_left) == 1
    assert right.distance(top_right) == right.distance(bottom_right) == 1

    assert bottom_right.distance(bottom_left) == top_right.distance(top_left) == 1


@given(hexagons())
def test_one_over(h):
    left = h.left()
    right = h.right()

    top_left = h.top_left()
    bottom_right = h.bottom_right()

    bottom_left = h.bottom_left()
    top_right = h.top_right()

    assert top_left.distance(bottom_left) == 2
    assert top_right.distance(bottom_right) == 2

    assert left.distance(bottom_right) == left.distance(top_right) == 2
    assert right.distance(bottom_left) == right.distance(top_left) == 2


@given(
    integers(min_value=2, max_value=10),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_straight_distance(i, d):
    h1 = h2 = H(0, 0)
    for _ in range(i):
        h2 = h2.neighbour(HD[d])

    assert h1.distance(h2) == i
    assert h1.distance(h2) == h2.distance(h1)


@given(
    hexagons(),
    sampled_from([
        HD.right, HD.left,
        HD.top_right, HD.bottom_right,
        HD.top_left, HD.bottom_left]))
def test_hexagon_direction_by_enum(h, hd):
    assert h.neighbour(hd) == h + get_neighbour_step(hd)


@given(
    hexagons(),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_neighbour_by_attr(h, d):
    getattr(h, d)() == h.neighbour(HD[d])
