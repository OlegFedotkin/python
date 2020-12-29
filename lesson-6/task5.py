# 5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'ООП упрощает сложный код,')

class Pencil(Stationery):
    def draw(self):
        print(f'но усложняет простой, мозг взорвался на этом ДЗ.')

class Handle(Stationery):
    def draw(self):
        print(f'Он отказывается понимать, зачем усложнять код!')

st = Stationery(1)
st.draw()

pn = Pen(2)
pn.draw()

pl = Pencil(100)
pl.draw()

hl = Handle()
hl.draw()
