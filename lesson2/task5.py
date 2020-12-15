# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,mont
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 5, 4, 3, 2, 1]
while True:
    number = int(input("Введите новый элемент рейтинга (если рейтинг заполнен - введите '0'): "))
    if number == 0:
        print(my_list)
        break
    elif number in my_list:
        number_ind = my_list.index(number) + my_list.count(number)
        my_list.insert(number_ind, number)
        print(my_list)
    else:
        new_list = my_list.copy()
        new_list.append(number)
        new_list.sort(reverse=True)
        elem = new_list.index(number)
        my_list.insert(elem, number)
        print(my_list)