def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            if result:
                yield result


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': None, 'color': 'white'},
        {'title': 'Стеллаж', 'price': 7000}
    ]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
    print(list(field(goods, 'price', 'color')))
