import sys
import math


def to_float(text):
    try:
        return float(text)
    except ValueError:
        return None


def ask_coef(prompt):
    value = to_float(input(prompt))
    match value:
        case None:
            print('Нужно ввести число, попробуйте еще раз')
            return ask_coef(prompt)
        case _:
            return value


def get_coef(index, prompt):
    match sys.argv[index:index + 1]:
        case [text] if to_float(text) is not None:
            return to_float(text)
        case [text]:
            print('Некорректное значение в командной строке:', text)
            return ask_coef(prompt)
        case _:
            return ask_coef(prompt)


def square_roots(a, b, c):
    match (a, b):
        case (0, 0):
            return []
        case (0, _):
            return [-c / b]

    d = b * b - 4 * a * c
    print('Дискриминант D =', d)
    match d:
        case d if d < 0:
            return []
        case 0:
            return [-b / (2 * a)]
        case _:
            return [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]


def roots_from_t(t):
    match t:
        case t if t > 0:
            return [math.sqrt(t), -math.sqrt(t)]
        case 0:
            return [0.0]
        case _:
            return []


def get_roots(a, b, c):
    all_roots = [x for t in square_roots(a, b, c) for x in roots_from_t(t)]
    return sorted(set(all_roots))


def print_roots(roots):
    match roots:
        case []:
            print('Действительных корней нет')
        case _:
            print('Количество корней:', len(roots))
            for i, root in enumerate(roots, 1):
                print(f'x{i} = {root}')


def main():
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    match (a, b):
        case (0, 0):
            print('Коэффициенты A и B равны нулю, это не уравнение')
        case _:
            print_roots(get_roots(a, b, c))


if __name__ == '__main__':
    main()
