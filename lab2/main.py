from tabulate import tabulate

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

N = 1


def main():
    r = Rectangle(N, N, 'синего')
    c = Circle(N, 'зеленого')
    s = Square(N, 'красного')
    print(r)
    print(c)
    print(s)

    print()
    table = [[f.get_figure_type(), f.fc.color, round(f.square(), 3)] for f in (r, c, s)]
    print(tabulate(table, headers=['Фигура', 'Цвет', 'Площадь'], tablefmt='grid'))


if __name__ == '__main__':
    main()
