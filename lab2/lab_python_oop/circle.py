import math

from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Circle(Figure):
    FIGURE_TYPE = 'Круг'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, color):
        self.radius = radius
        self.fc = FigureColor()
        self.fc.color = color

    def square(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиусом {}, площадь {:.3f}.'.format(
            self.get_figure_type(),
            self.fc.color,
            self.radius,
            self.square()
        )
