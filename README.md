# Лабораторная работа №3. Функциональные возможности языка Python

Арифулов Р.Х., группа ИУ5-31Б

Дисциплина: Парадигмы и конструкции языков программирования

## Цель работы

Изучение возможностей функционального программирования в языке Python.

## Задание

По ТЗ это одна работа на две лабы (№3–4) из 7 задач. Здесь сделаны **задачи 1–4**, а задачи 5–7 находятся в ветке [`lab4`](../../tree/lab4).

Все решения лежат в пакете `lab_python_fp`, каждая задача в своем файле. Если запустить файл, он выводит тестовые результаты.

## Структура

```
lab3/
└── lab_python_fp/
    ├── __init__.py
    ├── field.py        # задача 1
    ├── gen_random.py   # задача 2
    ├── unique.py       # задача 3
    └── sort.py         # задача 4
report/
├── lab3_report.docx
├── lab3_report.pdf
└── img/
```

## Задача 1. Генератор `field` (field.py)

`field(items, *args)` проходит по списку словарей и выдает значения указанных полей.

- Если передано одно поле, выдаются только значения, а `None` пропускается.
- Если полей несколько, выдаются словари только с этими полями. Поля со значением `None` в словарь не попадают, а если все поля `None`, элемент пропускается целиком.

```python
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
]
list(field(goods, 'title'))           # ['Ковер', 'Диван для отдыха']
list(field(goods, 'title', 'price'))  # [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}]
```

## Задача 2. Генератор `gen_random` (gen_random.py)

`gen_random(num_count, begin, end)` выдает `num_count` случайных целых чисел от `begin` до `end` включительно (через `random.randint`).

```python
list(gen_random(5, 1, 3))  # например [3, 3, 2, 1, 3]
```

## Задача 3. Итератор `Unique` (unique.py)

`Unique(items, **kwargs)` пропускает дубликаты. Работает и со списками, и с генераторами, потому что в конструкторе от данных берется `iter()`.

- Уже встреченные элементы запоминаются в множестве `seen`.
- Параметр `ignore_case` передается через `**kwargs`, по умолчанию `False`. Если он `True`, строки сравниваются в нижнем регистре, но возвращаются в исходном виде.

```python
list(Unique([1, 1, 2, 2, 2]))                                    # [1, 2]
list(Unique(['a', 'A', 'b', 'B', 'a']))                          # ['a', 'A', 'b', 'B']
list(Unique(['a', 'A', 'b', 'B', 'a'], ignore_case=True))        # ['a', 'b']
```

## Задача 4. Сортировка по модулю (sort.py)

Массив нужно отсортировать по модулю по убыванию одной строкой через `sorted`, двумя способами:

```python
result = sorted(data, key=abs, reverse=True)                          # без lambda
result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)  # с lambda
```

## Запуск

Внешние пакеты не нужны. Файлы запускаются из папки пакета, потому что `unique.py` импортирует `gen_random` напрямую:

```bash
cd lab3/lab_python_fp
python field.py
python gen_random.py
python unique.py
python sort.py
```

## Пример работы

```
> python field.py
['Ковер', 'Диван для отдыха', 'Стеллаж']
[{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}, {'title': 'Стеллаж', 'price': 7000}]
[{'price': 2000, 'color': 'green'}, {'color': 'black'}, {'color': 'white'}, {'price': 7000}]

> python unique.py
[1, 2]
[3, 1, 2]
['a', 'A', 'b', 'B']
['a', 'b']

> python sort.py
[123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
[123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
```

## Отчет

- [lab3_report.pdf](report/lab3_report.pdf)
- [lab3_report.docx](report/lab3_report.docx)
