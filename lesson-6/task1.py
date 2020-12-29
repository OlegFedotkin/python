# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color[0] != 'Red' or self.__color[1] != 'Yellow' or self.__color[2] != 'Green':
            print(f'Светофор работает неверно!')
        else:
            for i in self.__color:
                if i == 'Red':
                    print('Red')
                    sleep(7)
                if i == 'Yellow':
                    print('Yellow')
                    sleep(2)
                if i == 'Green':
                    print('Green')
                    sleep(10)

tl = TrafficLight(['Red', 'Yellow', 'Green'])
tl.running()