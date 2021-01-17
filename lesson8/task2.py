class GetPointError(Exception):
    def __init__(self, zero):
        self.zero = zero


my_number = int(input('Введите число: '))

try:
    if my_number == 0:
        raise GetPointError('Нельзя делить на ноль!')
except ValueError:
    print('Вы ввели не число!')
except GetPointError as err:
    print(err)
else:
    print(f'Ответ: {100000 / my_number}')