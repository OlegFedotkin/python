# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from earning import earning_function

zp = earning_function(160, 0.99, 99)

print(f'Заработная плата составляет {zp} руб. месяц')