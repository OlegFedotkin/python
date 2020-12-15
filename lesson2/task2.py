#2) Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
item = True
while item != 'End':
    item = input("Введите элемент списка (если список заполнен - введите 'End'): ")
    my_list.append(item)

print(my_list)

elem = 0
for num in range(len(my_list) // 2):
    my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
    elem += 2

print(my_list)
