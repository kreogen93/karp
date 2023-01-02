# Добавьте в класс возможности сравнивать два вектора между собой и считать abs (это длина вектора, в Евклидовой метрике).


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

    def __str__(self):
        return str(self.coords)

    def __mul__(self, other):
        if isinstance(other, Vector):
            _l, _r = len(self.coords), len(other.coords)
            if len(self.coords) != len(other.coords):
                raise ValueError(f"left and right lengths differ: {_l} != {_r}")
            result = 0
            for i in range(len(self.coords)):
                result += self.coords[i] * other.coords[i]
            return result
        else:
            return Vector([x * other for x in self.coords])

    def __repr__(self):
        return self.__str__()

    def __abs__(self):
        return sum([x ** 2 for x in self.coords]) ** 0.5

    def __eq__(self, other):
        return self.coords == other.coords