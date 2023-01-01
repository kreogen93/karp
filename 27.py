# Создайте класс Rectangle (прямоугольник), который будет наследоваться от класса Triangle.
# Сделайте так, чтобы area(), конструктор и поле n_dots были верными. А именно:
# Конструктор должен принимать 2 стороны: a, b
# area() должен считать площадь как произведение смежных сторон: S=ab
# Неравенство треугольника не нужно проверять.
# n_dots должен быть объявлен на уровне класса и равняться 4.
class Triangle:
    n_dots = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a <= b + c and b <= a + c and c <= a + b:
            raise ValueError("triangle inequality does not hold")

    def area(self):
        p = 0.5 * (self.a + self.b + self.c)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class Rectangle(Triangle):
    n_dots = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b