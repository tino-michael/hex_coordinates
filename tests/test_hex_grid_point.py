import pytest
from hex_grid.hex_grid_points import HexGridPoint as P

from hypothesis import given
from hypothesis.strategies import integers, floats


@given(integers(), integers())
def test_hex_grid_point_slice(a, b):
    assert P(a, b) == P(a, b, -a-b)
    assert P(a, b).get_rst() == (a, b, -a-b)


@given(integers(), integers(), integers(), integers())
def test_hex_grid_point_addition_(a, b, x, y):
    assert P(a, b) + P(x, y) == P(a+x, b+y)


@given(integers(), integers(), integers(), integers())
def test_hex_grid_point_subtraction(a, b, x, y):
    assert P(a, b) - P(x, y) == P(a-x, b-y)


@given(integers(), integers(), integers())
def test_hex_grid_point_multiplication_integer(a, b, c):
    assert P(a, b) * c == P(a*c, b*c)
    assert a * P(b, c) == P(a*b, a*c)


@given(integers(), integers(), floats())
def test_hex_grid_point_multiplication_float(a, b, c):
    P(a, b, offgrid=True) * c
    with pytest.raises(TypeError):
        P(a, b) * c


@given(integers(), integers(), integers(), integers())
def test_hex_grid_point_multiplication_hexpoint(a, b, x, y):
    with pytest.raises(TypeError):
        P(a, b) * P(x, y)
