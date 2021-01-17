class GetPointError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    my_number = input("Введите число (для остановки цикла введите 'stop'): ")
    if my_number == 'stop':
        break
    try:
        if my_number.isdigit():
            my_list.append(int(my_number))
        else:
            raise GetPointError('Введено строковое значение!')
    except GetPointError as err:
        print(err)

print(my_list)