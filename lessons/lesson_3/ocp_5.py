import abc


# Абстрактная фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


# Круг
class Circle(Figure):
    def draw(self):
        pass


# Треугольник
class Triangle(Figure):
    def draw(self):
        pass


class Romb(Figure):
    def draw(self):
        pass


class Line(Figure):
    def draw(self):
        pass


class Line(Figure):
    def draw(self):
        pass


class Square(Figure):
    def draw(self):
        pass


class Romb(Figure):
    def draw(self):
        pass


# САПР
class CAD:
    @classmethod
    def draw_all(cls, figures):
        for figure in figures:
            figure.draw()
