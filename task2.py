#2) Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input('Введите время в секундах '))
hours = seconds // 3600
minites = (seconds % 3600) // 60
rest_seconds = (seconds % 3600) % 60
print(f'{hours}:{minites}:{rest_seconds}')