"""
The slice of the Hexagon's cube coordinates -- i.e. the sum of all three coordinates.
Do not change from 0, otherwise arithmetic (+, -, *) won't work!
"""
SLICE = 0


class HexGridPoint():
    def __init__(self, r, s, t=None, offgrid: bool = False):

        if t is None:
            t = SLICE - r - s
        elif offgrid:
            pass
        else:
            if r + s + t != SLICE:
                raise ValueError("wrong slice: {r+s+t} != {SLICE}")

        self.r = r
        self.s = s
        self.t = t
        self.offgrid = offgrid

    def get_rst(self):
        return (self.r, self.s, self.t)

    def __neg__(self):
        r, s, t = self.get_rst()
        return self.__class__(-r, -s, -t)

    def __add__(self, other):
        r1, s1, t1 = self.get_rst()
        r2, s2, t2 = other.get_rst()

        return self.__class__(r1+r2, s1+s2, t1+t2, offgrid=(self.offgrid or other.offgrid))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other: int | float):
        # Allow multiplication with integers always and with floats only when `offgrid` is True.
        if not (isinstance(other, int) or (isinstance(other, float) and self.offgrid)):
            raise TypeError
        r, s, t = self.get_rst()
        return self.__class__(r*other, s*other, t*other, offgrid=self.offgrid)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        r, s, t = self.get_rst()
        return self.__class__(r/other, s/other, t/other, offgrid=self.offgrid)

    def __eq__(self, other):
        r1, s1, t1 = self.get_rst()
        r2, s2, t2 = other.get_rst()

        return r1 == r2 and s1 == s2 and t1 == t2

    def distance(self, other):
        r1, s1, t1 = self.get_rst()
        r2, s2, t2 = other.get_rst()

        return sum([
            abs(r1 - r2),
            abs(s1 - s2),
            abs(t1 - t2)
        ]) / 2.
