# Перепишите классы Triangle, Rectangle так, чтобы они наследовались от BaseFigure.
# Затем уберите реализацию всех методов и конструкторов в классах-потомках.


class BaseFigure:
    n_dots = None

    def area(self):
        raise NotImplementedError()

    def validate(self):
        raise NotImplementedError()

    def __init__(self):
        self.validate()


class Triangle(BaseFigure):
    pass


class Rectangle(BaseFigure):
    pass