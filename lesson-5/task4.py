# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('for_task4.txt', 'r', encoding='utf-8') as table:
    inp_str = table.readlines()

number = []
eng_list = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'}
list_key = eng_list.keys()

for i in inp_str:
    for j in list_key:
        if j in i:
           k = i.replace(j, eng_list.get(j))
    number.append(k)

with open('update_for_task4.txt', 'w') as task4_txt:
    task4_txt.writelines(number)
