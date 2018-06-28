from utils.time_utils import *


def dedupe(items):
    """
    在一个序列上面保持元素顺序的同时消除重复的值
    :param items:
    :return:
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_not_hashable(items, key=None):
    """
    在一个not hashable序列上面保持元素顺序的同时消除重复的值
    :param items:
    :param key:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    with timer('test dedupe hashable data use set'):
        a = [1, 5, 2, 1, 9, 1, 5, 10]
        print(f'raw list is: {a}\n'
              f'dedupe list is: {list(dedupe(a))}')

    with timer('test dedupe not hashable data use set'):
        a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        key = lambda d: (d['x'], d['y'])
        print(f'raw list is: {a}\n'
              f'dedupe list is: {list(dedupe_not_hashable(a, key=key))}')


