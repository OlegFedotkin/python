# 4) Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func_1(x, y):
    result_1 = x ** y
    result_mean = x
    z = abs(y + 1)
    if y == -1:
        result_2 = 1 / x
    else:
        for el in range(z):
            result_mean *= x
        result_2 = 1 / result_mean
    return result_1, result_2


result = my_func_1(2, -4)
print(result)