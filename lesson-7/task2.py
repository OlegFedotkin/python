# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def size_coat(self):
        pass
    @abstractmethod
    def size_suit(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def size_coat(self):
        size = round(self.v / 6.5 + 0.5, 2)
        return size

    def size_suit(self):
        pass

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def size_suit(self):
        height = round(2 * self.h / 100 + 0.3, 2)
        return height

    def size_coat(self):
        pass

mc = Coat(48)
mc1 = Suit(173)

print(mc.size_coat)
print(mc1.size_suit)