# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, age, city, email, phone):
    print(f'Данные пользователя: имя - {name}, фамилия - {surname}, год рождения - {age}, город проживания - {city}, email - {email}, телефон - {phone}')

user_data(name='Остап', surname='Бендер', age=36, city='Черноморск', email='drthdrh@yan.com', phone=66666666666)