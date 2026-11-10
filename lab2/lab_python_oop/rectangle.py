from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = 'Прямоугольник'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.fc = FigureColor()
        self.fc.color = color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {}, площадь {}.'.format(
            self.get_figure_type(),
            self.fc.color,
            self.width,
            self.height,
            self.square()
        )
