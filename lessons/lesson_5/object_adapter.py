from abc import ABCMeta, abstractmethod
from math import sqrt


# нечто круглое, имеющее радиус
class Roundable(metaclass=ABCMeta):
    @abstractmethod
    def get_radius(self):
        pass


# окружность - имеет радиус
class Circle(Roundable):
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


# квадрат со стороной side
class Square:
    def __init__(self, side):
        self._side = side

    def get_side(self):
        return self._side


# адаптер квадрата к круглым фигурам
class RoundableAdapter(Roundable):
    def __init__(self, adaptee):
        self._adaptee = adaptee
        print(self._adaptee)

    # радиус квадрата - как радиус описанной окружности
    def get_radius(self):
        return self._adaptee.get_side() * sqrt(2) / 2


# список окружностей и квадратов
figures_1 = [Circle(5), Square(5), Circle(2), Square(2)]
