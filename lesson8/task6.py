
class GetPointError(Exception):
    def __init__(self, zero):
        self.zero = zero

class Warehouse:

    @staticmethod
    def get_warehouse(my_dict, name, quantity):
        my_dict[name] += quantity
        return f'На склад поступило {quantity} ед. {name}'

    @staticmethod
    def give_warehouse(my_dict, name, quantity):
        negative = my_dict[name] - quantity
        try:
            if negative < 0:
                raise GetPointError('Остаток на складе меньше нуля, введите верное количество')
        except GetPointError as err:
            print(err)
        else:
            my_dict[name] -= quantity
            return f'Передано в подразделение {quantity} ед. {name}'

class OfficeEquipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Название: {self.name}, количество: {self.quantity}"

class Printer(OfficeEquipment):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self.price = price

class Scaner(OfficeEquipment):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self.price = price

class Copier(OfficeEquipment):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self.price = price

warehouse = {'printer': 0, 'scaner': 0, 'copier': 0}

o = OfficeEquipment('OfficeEquipment', 15)
print(o)
p = Printer('Xerox', 4, 15698)
print(p)
s = Scaner('Canon', 6, 12365)
print(s)
c = Copier('Kyocera', 5, 5699)
print(c)
print(f'{p}, {s}, {c}')

warehouse = {'printer': 4, 'scaner': 6, 'copier': 5}
name = input("Введите название оргтехники: ")
quantity = int(input("Введите количество оргтехники: "))
print(Warehouse.give_warehouse(warehouse, name, quantity))

