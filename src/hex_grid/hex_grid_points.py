from dataclasses import dataclass


@dataclass
class HexGridPoint():
    r : int
    s : int
    t : int

    def get_rst(self):
        return (self.r, self.s, self.t)

    def __neg__(self):
        r, s, t = self.get_rst()
        return self.__class__(-r, -s, -t)

    def __add__(self, other):
        r1, s1, t1 = self.get_rst()
        r2, s2, t2 = other.get_rst()

        return self.__class__(r1+r2, s1+s2, t1+t2)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other : int):
        if isinstance(other, int):
            r, s, t = self.get_rst()
            return self.__class__(r*other, s*other, t*other)
        raise TypeError("unsupported operand type")

    def __rmul__(self, other):
        return self.__mul__(other)
