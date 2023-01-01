# Возьмите класс Triangle из предыдущего задания и добавьте метод area(), возвращающий площадь треугольника.
# Напомним, что при известных трех сторонах площадь треугольника можно подсчитать по формуле Герона: S=
# sqrt(p(p−a)(p−b)(p−c)), где p= 0.5(a+b+c) - полупериметр. Подумайте, как можно организовать код так,
# чтобы p считалась один раз.
# Затем поменяйте конструктор: он должен проверять, что выполнено неравенство треугольника - каждая сторона меньше или
# равна сумме двух других. Если это условие не выполнено, выбрасывайте ValueError с текстом
# "triangle inequality does not hold" (передайте эту строку в конструктор ValueError).


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
