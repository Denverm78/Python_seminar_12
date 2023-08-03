# Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

import json

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


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("new_json.json", "w", encoding="utf-8") as file:
            json.dump(self.dictn, file, indent=2)
        print("Завершено")


with Factorial(5) as f:
    print(f(10))

print(f)