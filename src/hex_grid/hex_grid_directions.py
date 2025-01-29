from .hex_enums import HexDirection
from .hex_grid_points import HexGridPoint


def get_neighbour_step(dir: HexDirection) -> HexGridPoint:
    match dir:
        case HexDirection.right:
            return HexGridPoint(1, 0, -1)
        case HexDirection.left:
            return HexGridPoint(-1, 0, 1)
        case HexDirection.top_right:
            return HexGridPoint(1, -1, 0)
        case HexDirection.bottom_right:
            return HexGridPoint(0, 1, -1)
        case HexDirection.top_left:
            return HexGridPoint(0, -1, 1)
        case HexDirection.bottom_left:
            return HexGridPoint(-1, 1, 0)
        case _:
            raise ValueError()
