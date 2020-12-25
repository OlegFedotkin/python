# 6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

with open('for_task6.txt', 'r', encoding='utf-8') as table:
    my_list = table.readlines()

result = []
for el in my_list:
    length = len(el)
    i = 0
    integ = []
    while i < length:
        s_int = ''
        elem = el[i]
        while '0' <= elem <= '9':
            s_int += elem
            i += 1
            if i < length:
                elem = el[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    result.append(sum(integ))

next_list = []
for el in my_list:
    next_list.append(el.split(':'))

second_list = []
for el in next_list:
    second_list.append(el[0])

my_dict = {second_list[i]: result[i] for i in range(0, len(second_list))}

print(f'Итог: {my_dict}')