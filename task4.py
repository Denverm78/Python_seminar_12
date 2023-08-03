# Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль
# недопустимых значений (отрицательных).
# 📌 Используйте декораторы свойств.

class rectangle():
    
    def __init__(self, a, b):
        self._a = a
        self._b = b
        self.min = 0

    @property
    def side_a(self):
        return self._a

    @property
    def side_b(self):
        return self._b

    @side_a.setter
    def side_a(self, value):
        if value > self.min:
            self._a = value
        else:
            raise ValueError(f'Значение должно быть больше 0: {self._a}')

    @side_b.setter
    def side_b(self, value):
        if value > self.min:
            self._b = value
        else:
            raise ValueError(f'Значение должно быть больше 0: {self._b}')


pr1 = rectangle(2, 4)
pr2 = rectangle(4, 2)
print(pr1.side_a)
print(pr1.side_b)
pr1.side_a = 5
print(pr1.side_a)
pr1.side_b = 10
print(pr1.side_b)