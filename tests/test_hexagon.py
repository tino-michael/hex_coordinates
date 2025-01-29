import pytest
from hypothesis import given
from hypothesis.strategies import integers, floats, sampled_from
from .hex_strategies import hexagons

from hex_grid import (
    HexDirection as HD,
)

from hex_grid.hex_grid_directions import get_neighbour_step


@given(
    hexagons(),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_neighbour_distance(h1, d):
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
    hexagons(),
    integers(min_value=2, max_value=10),
    sampled_from([
        "right", "left",
        "top_right", "bottom_right",
        "top_left", "bottom_left"]))
def test_hexagon_straight_distance(h1, i, d):
    h2 = h1
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


@given(hexagons(), integers())
def test_hexagon_point_multiplication_integer(h, i):
    h * i


@given(hexagons(), floats())
def test_hexagon_point_multiplication_float(h, f):
    with pytest.raises(TypeError):
        h * f


@given(hexagons(), hexagons())
def test_hexagon_point_multiplication_hexagon(h1, h2):
    with pytest.raises(TypeError):
        h1 * h2
