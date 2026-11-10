import sys
import math


class BiquadraticEquation:

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = None
        self.roots = []

    def read_coef(self, index, prompt):
        if index < len(sys.argv):
            try:
                return float(sys.argv[index])
            except ValueError:
                print('Некорректное значение в командной строке:', sys.argv[index])

        while True:
            text = input(prompt)
            try:
                return float(text)
            except ValueError:
                print('Нужно ввести число, попробуйте еще раз')

    def read_all(self):
        self.a = self.read_coef(1, 'Введите коэффициент А: ')
        self.b = self.read_coef(2, 'Введите коэффициент B: ')
        self.c = self.read_coef(3, 'Введите коэффициент C: ')

    def solve_square(self):
        # корни для t = x^2
        if self.a == 0:
            return [-self.c / self.b]
        self.d = self.b * self.b - 4 * self.a * self.c
        if self.d < 0:
            return []
        if self.d == 0:
            return [-self.b / (2 * self.a)]
        sqrt_d = math.sqrt(self.d)
        return [(-self.b + sqrt_d) / (2 * self.a), (-self.b - sqrt_d) / (2 * self.a)]

    def calculate(self):
        result = set()
        for t in self.solve_square():
            if t > 0:
                result.add(math.sqrt(t))
                result.add(-math.sqrt(t))
            elif t == 0:
                result.add(0.0)
        self.roots = sorted(result)

    def print_roots(self):
        if self.d is not None:
            print('Дискриминант D =', self.d)
        if len(self.roots) == 0:
            print('Действительных корней нет')
        else:
            print('Количество корней:', len(self.roots))
            for i, root in enumerate(self.roots, 1):
                print(f'x{i} = {root}')


def main():
    eq = BiquadraticEquation()
    eq.read_all()
    if eq.a == 0 and eq.b == 0:
        print('Коэффициенты A и B равны нулю, это не уравнение')
        return
    eq.calculate()
    eq.print_roots()


if __name__ == '__main__':
    main()
