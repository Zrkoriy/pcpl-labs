import sys
import math


def get_coef(index, prompt):
    # сначала пробуем взять коэффициент из командной строки
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


def get_roots(a, b, c):
    result = []
    if a == 0:
        # уравнение вырождается в b*x^2 + c = 0
        if b == 0:
            return result
        t_list = [-c / b]
    else:
        d = b * b - 4 * a * c
        print('Дискриминант D =', d)
        if d < 0:
            return result
        if d == 0:
            t_list = [-b / (2 * a)]
        else:
            sqrt_d = math.sqrt(d)
            t_list = [(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)]

    for t in t_list:
        if t > 0:
            x = math.sqrt(t)
            result.append(x)
            result.append(-x)
        elif t == 0:
            result.append(0.0)

    return sorted(set(result))


def main():
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    if a == 0 and b == 0:
        print('Коэффициенты A и B равны нулю, это не уравнение')
        return

    roots = get_roots(a, b, c)
    if len(roots) == 0:
        print('Действительных корней нет')
    else:
        print('Количество корней:', len(roots))
        for i, root in enumerate(roots, 1):
            print(f'x{i} = {root}')


if __name__ == '__main__':
    main()

# Пример запуска
# python procedural.py 1 -5 4
