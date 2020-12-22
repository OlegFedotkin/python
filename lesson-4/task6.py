# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

for el in count(14):
    if el > 31:
        break
    else:
        print(el)


my_list = ['go', 'ahead']
k = 0
for el in cycle(my_list):
    if k > 20:
        break
    else:
        print(el)
    k += 1