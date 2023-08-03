# Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

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


class Factorial_gen:

    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += self.step
            p = Factorial(5)
            print(self.start)
            return p(self.start)
        else:
            raise StopIteration


    
fact = Factorial_gen(10, 2, 2)
for f in fact:
    print(f)