# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(numer, denom):
    return numer / denom

numerator = int(input('Введите числитель: '))
denominator = int(input('Введите знаменатель: '))
if denominator == 0:
    print('На ноль делить нельзя!')
else:
    answer = round(my_func(numerator, denominator), 2)
    print(f'Ответ: {answer}')