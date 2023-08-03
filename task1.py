# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

class Factorial:

    def __init__(self, k):
        self.k = k
        self.start = 1
        self.dictn = {self.start: 1}


    def __call__(self, n, *args, **kwargs):
        self.start = 1
        for i in range(1, n + 1):
            self.start *= i
            self.dictn[i] = self.start
            if len(self.dictn) >= self.k:
                self.dictn.pop(i - self.k, 0)
        return self.start


    def __str__(self):
        return f'{self.dictn}'


f =  Factorial(6)
print(f(12))
print(f)