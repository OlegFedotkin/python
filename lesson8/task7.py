class ComplexInt:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


a = complex(3, 4)
b = complex(5, 6)
comp1 = ComplexInt(a)
comp2 = ComplexInt(b)
print(comp1 + comp2)
print(comp1 * comp2)