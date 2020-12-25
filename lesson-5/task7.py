# 7) Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

import json

my_list =[]

with open('for_task7.txt', 'r', encoding='utf-8') as table:
    for line in table:
        my_list.append(line)

next_list = []
for el in my_list:
    next_list.append(el.split('   '))

second_list = []
for el in next_list:
    second_list.append(el[0])

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
    result.append(integ[1] - integ[2])

my_dict = {second_list[i]: result[i] for i in range(0, len(second_list))}

average_prof = 0
count_firm = 0
for el in result:
    if el >= 0:
        average_prof += el
        count_firm += 1

average = average_prof / count_firm

new_dict = {'average_profit': average}

result_list = [my_dict, new_dict]

print(result_list)



with open('task7.json', 'w') as json_dump:
    json.dump(result_list, json_dump)
