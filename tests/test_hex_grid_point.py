from hex_coordinates.hex_grid_points import HexGridPoint as P

from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers(), integers(), integers(), integers(), integers())
def test_hex_grid_point_addition(a, b, c, x, y, z):
    assert P(a, b, c) + P(x, y, z) == P(a+x, b+y, c+z)

    rst = (P(a, b, c) + P(x, y, z)).get_rst()
    assert rst == (a+x, b+y, c+z)
