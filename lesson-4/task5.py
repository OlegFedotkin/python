# 5) Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

def multiplication(one, two):
    return one * two

my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(multiplication, my_list))
