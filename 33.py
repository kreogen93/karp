# Добавьте методу красивый вывод при передаче его в print(...)


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