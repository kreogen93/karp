# Возьмите классы Triangle и Rectangle из прошлого задания.
# Переопределите метод area в каждом случае.
# Переопределите конструктор в каждом случае (число аргументов тоже меняется).
# Не забудьте в конструкторе дочернего класса вызвать конструктор родительского класса!
# Переопределите метод validate в каждом случае. Метод validate должен принимать только аргумент self
# и использовать созданные в конструкторе переменные.Для этого вы можете сначала сохранять в конструкторе входные данные
# в self.переменная, а затем вызывать конструктор суперкласса. Для Triangle данный метод должен проверять неравенство
# треугольника и выбрасывать ошибку ValueError("triangle inequality does not hold") либо возвращать значения сторон.
# Для Rectangle данный метод должен возвращать значения сторон.
# В итоге вы получите два класса, которые построены по схожему шаблону. Этот общий шаблон был задан в классе BaseFigure.
# Создайте несколько объектов этих классов и попробуйте вызвать у них .area(), .validate().
# Если вы пользуетесь IDE, то увидите интерактивные подсказки: она скажет, что такие методы есть и что эти
# методы перегружают (overload) методы из родительского класса. При этом вызов методов будет работать коррректно.


class BaseFigure:
    n_dots = None

    def area(self):
        raise NotImplementedError()

    def validate(self):
        raise NotImplementedError()

    def __init__(self):
        self.validate()

class Triangle(BaseFigure):
    n_dots = 3

    def area(self):
        p = 0.5 * (self.a + self.b + self.c)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def validate(self):
        a_, b_, c_ = sorted([self.a, self.b, self.c])
        if c_ > a_ + b_:
            raise ValueError("triangle inequality does not hold")

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        super().__init__()


class Rectangle(BaseFigure):
    n_dots = 4

    def area(self):
        return self.a * self.b

    def validate(self):
        pass

    def __init__(self, a, b):
        self.a, self.b = a, b
        super().__init__()