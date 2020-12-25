# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers = '5 69 45 87 2 36 4 58.1 52'

with open('for_task5.txt', 'w') as task5_txt:
    task5_txt.write(numbers)

with open('for_task5.txt', 'r', encoding='utf-8') as table:
    inp_str = table.read()

my_list = inp_str.split(' ')

new_list = []
for el in my_list:
    new_list.append(float(el))

result = sum(new_list)

print(f'Сумма чисел равна: {result}')
