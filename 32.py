# Напишите класс Vector, который на вход будет принимать список координат.
# Положите все координаты вектора в список self.coords.
# Добейтесь того, чтобы объекты класса Vector можно было складывать через оператор + и получать
# на выходе тоже объект этого же класса.


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