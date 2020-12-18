# 6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(word):
    my_str = word.capitalize()
    return my_str


def int_func_update(word):
    my_list = word.split()
    new_list = []
    for el in my_list:
        elem = int_func(el)
        new_list.append(elem)
    new_list = ' '.join(new_list)
    return new_list


result_1 = int_func('text')
print(result_1)

result_2 = int_func_update('программа запрашивает у пользователя строку чисел')
print(result_2)