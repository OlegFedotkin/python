#3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = int(input('Введите номер в виде целого числа от 1 до 12: '))
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]

if month in spring:
    print('Весна')
elif month in summer:
    print('Лето')
elif month in autumn:
    print('Осень')
elif month in winter:
    print('Зима')
else:
    print('Неверно указан номер месяца')


seasons = {
1: 'Зима',
2: 'Зима',
3: 'Весна',
4: 'Весна',
5: 'Весна',
6: 'Лето',
7: 'Лето',
8: 'Лето',
9: 'Осень',
10: 'Осень',
11: 'Осень',
12: 'Зима'}

for item in seasons:
    if item == month:
        print(seasons.get(item))