# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('for_task2.txt', 'r', encoding='utf-8') as txt_task:
    my_list = txt_task.readlines()

str_num = 0
for el in my_list:
    str_num += 1
    word_count = len(el.split(' '))
    print(f'Количество слов в {str_num} строке: {word_count}')
str_count = len(my_list)
print(f'Количество строк равно: {str_count}')
