# Добавьте в класс возможность умножать вектор на вектор и вектор на число.


class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __add__(self, other):
        _l, _r = len(self.coords), len(other.coords)
        if _l != _r:
            raise ValueError(f"left and right lengths differ: {_l} != {_r}")
        return Vector([
            self.coords[i] + other.coords[i]
            for i in range(len(self.coords))
        ])

    def __repr__(self):
        return str(self.coords)

    def __mul__(self, other):
        if isinstance(other, Vector):
            _l, _r = len(self.coords), len(other.coords)
            if _l != _r:
                raise ValueError(f"left and right lengths differ: {_l} != {_r}")
            result = 0
            for i in range(len(self.coords)):
                result += self.coords[i] * other.coords[i]
            return result
        else:
            return Vector([x * other for x in self.coords])