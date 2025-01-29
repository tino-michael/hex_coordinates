from hypothesis import given
from .hex_strategies import hexagons


@given(hexagons())
def test_hexagon_shared_vertices(h):
    h_r = h.right()
    h_l = h.left()
    h_tr = h.top_right()
    h_tl = h.top_left()
    h_br = h.bottom_right()
    h_bl = h.bottom_left()

    # center and right
    assert h.top_right_vertex() == h_r.top_left_vertex()
    assert h.bottom_right_vertex() == h_r.bottom_left_vertex()

    # center and left
    assert h.top_left_vertex() == h_l.top_right_vertex()
    assert h.bottom_left_vertex() == h_l.bottom_right_vertex()

    # center and top-right
    assert h.top_right_vertex() == h_tr.bottom_vertex()
    assert h.top_vertex() == h_tr.bottom_left_vertex()

    # center and top-left
    assert h.top_left_vertex() == h_tl.bottom_vertex()
    assert h.top_vertex() == h_tl.bottom_right_vertex()

    # center and bottom-right
    assert h.bottom_right_vertex() == h_br.top_vertex()
    assert h.bottom_vertex() == h_br.top_left_vertex()

    # center and bottom-left
    assert h.bottom_left_vertex() == h_bl.top_vertex()
    assert h.bottom_vertex() == h_bl.top_right_vertex()
