# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Square:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number - other.number < 0:
            print(f'Разность меньше нуля!')
        else:
            return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return int(self.number / other.number)

    def make_order(self, count_in_range):
        pass

    def make_order(self, count_sq):
        elem_1 = int(self.number / count_sq)
        elem_2 = self.number %  count_sq
        my_str = ''
        for i in range(elem_1):
            my_str += ('*' * count_sq + '\n')
        my_str += '*' * elem_2
        return my_str

sq_1 = Square(12)
sq_2 = Square(5)
print(sq_1 + sq_2)
print(sq_1 - sq_2)
print(sq_1 * sq_2)
print(sq_1 / sq_2)
print(sq_1.make_order(2))