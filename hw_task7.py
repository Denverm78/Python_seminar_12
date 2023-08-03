# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.


import csv
from functools import reduce


class Validate:
    """Проверка ФИО на первую заглавную букву и наличие только букв"""
    
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно являться текстом')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно иметь первую заглавную букву')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')

class Student:
    """Создание класса Student с оценками по предметам и тестам"""
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _classes = None
    
    def __init__(self, second_name, first_name, surname):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname
        self.classes = 'classes.csv'

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, classes):
        self._classes = {'classes': {}}
        with open(classes, 'r', encoding='utf-8') as c_f:
            reader = csv.reader(c_f)
            for row in reader:
                self._classes['classes'][row[0]] = {'grades': [], 'tests': [], 'middle_grade_test': None}
        self._classes["middle_grade"] = None

    def new_grade(self, class_name, grade, type_grade: str = 'subj'):
        if class_name not in self.classes['classes'].keys():
            raise AttributeError('Такой предмет недопустим')
        if type_grade == "subj":
            if grade < 2 or grade > 5:
                raise ValueError('Оценка за предмет должна быть в диапазоне от 2 до 5')
            self.classes['classes'][class_name]['grades'].append(grade)
            self.classes['middle_grade'] = self.middle_grade(self.classes)
            # print(self.classes['middle_grade'])
        elif type_grade == 'test':
            if grade < 0 or grade > 100:
                raise ValueError('Оценка теста должна быть от 0 до 100')
            self.classes['classes'][class_name]['tests'].append(grade)
            self.classes['classes'][class_name]['middle_grade_test'] = \
                reduce(lambda x, y: x + y, self.classes['classes'][class_name]['tests']) / \
                len(self.classes['classes'][class_name]['tests'])


    """Вычисление средней оценки по предмету"""
    @staticmethod
    def middle_grade(classes):
        all_grades = []
        [all_grades.extend(classes["classes"][name]["grades"]) for name in classes["classes"]]
        return reduce(lambda x, y: x + y, all_grades) / len(all_grades)

    def __repr__(self):
        result = f"Студент - '{self.second_name} {self.first_name} {self.surname}'\n\
Средняя оценка по предметам = {self.classes['middle_grade']}\n"
        result += "Средние оценки по тестам: \n"
        for key, value in self.classes["classes"].items():
            result += f"{key}={value['middle_grade_test']}\n"
        return result



    
student1 = Student('Иванов', 'Петр', 'Николаевич')
student1.new_grade('Алгебра', 4)
student1.new_grade('Алгебра', 4)
student1.new_grade('Литература', 2)
student1.new_grade('Русский язык', 5)
student1.new_grade('Геометрия', 90, 'test')
student1.new_grade('Геометрия', 70, 'test')
# student1.new_grade('Биология', 75, 'test')
student1.new_grade('Литература', 60, 'test')
student1.new_grade('Русский язык', 100, 'test')
student1.new_grade('Алгебра', 55, 'test')
print(student1)
