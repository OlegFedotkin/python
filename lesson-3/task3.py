# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.sort(key=lambda number: number, reverse=True)
    summ = sum(my_list[:2])
    return summ

result = my_func(3, 6, 10)
print(result)