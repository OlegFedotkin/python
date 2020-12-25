# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('for_task3.txt', 'r', encoding='utf-8') as table:
    my_list = table.readlines()

new_list = []
for el in my_list:
    new_list.extend(el[0:-1].split(' '))

float_lst = []
for el in new_list:
    try:
        float_lst.append(float(el))
    except ValueError:
        float_lst.append(el)
        continue

my_dict = {float_lst[i]: float_lst[i + 1] for i in range(0, len(float_lst), 2)}

new_dict = {key: val for key, val in my_dict.items() if val < 20000}

print(f'Оклады менее 20000 у следующих сотрудников: {list(new_dict.keys())}')

result = round((sum(my_dict.values())) / len(my_dict.values()), 2)
print(f'Средняя зарплата {result}')