# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
        def get_full_name(self):
            full_name = self.name + ' ' + self.surname
            print(f'Имя и фамилия {full_name}')

        def get_total_income(self):
            total_income = sum(self._income.values())
            print(f'Зарплата {total_income}')

my_dict_1 = {'wage': 10000, 'bonus': 5000}
p1 = Position('Albert', 'Einstein', 'scientist', my_dict_1)
p1.get_full_name()
p1.get_total_income()

my_dict_2 = {'wage': 100, 'bonus': 5}
p2 = Position('Раб', 'Рабов', 'раб', my_dict_2)
p2.get_full_name()
p2.get_total_income()