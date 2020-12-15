# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

elem = 1
result_list = []
name = []
price = []
quantity = []
eded = ['шт.']
while True:
    my_list = []
    my_dict = {}
    name_value = input("Введите название товара (еcли каталог заполнен - введите '0'): ")
    if name_value == '0':
        break
    else:
        price_value = int(input("Введите цену товара: "))
        quantity_value = int(input("Введите количество товара: "))

        # список кортежей
        my_dict = dict(название=name_value, цена=price_value, количество=quantity_value, eд='шт.')
        my_list.append(elem)
        my_list.append(my_dict)
        my_tuple = tuple(my_list)
        result_list.append(my_tuple)
        elem += 1

        # аналитика товаров
        name.append(name_value)
        price.append(price_value)
        quantity.append(quantity_value)

new_dict = dict(название=name, цена=price, количество=quantity, eд=eded)

print(result_list)
print(new_dict)
