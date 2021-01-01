# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.cl

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return ('\n'.join(map(str, self.my_list)))

    def __add__(self, other):
        joined_list = []
        strings = []
        for el in range(len(self.my_list)):
            for elem in range(len(self.my_list[0])):
                sum_mat = other.my_list[el][elem] + self.my_list[el][elem]
                strings.append(sum_mat)
            joined_list.append(strings)
            strings = []
        return Matrix(joined_list)

first_list = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
sec_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
mt1 = Matrix(first_list)
mt2 = Matrix(sec_list)
print(mt1 + mt2)