from contextlib import contextmanager
import time
from collections import deque


@contextmanager
def timer(name):
    start = time.time()
    yield
    print(f'[{name} done in {time.time() - start :0.2} s]')


def drop_first_last(grades):
    first, *middles, last = grades
    return sum(middles) / len(middles)


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


def sum_recursive(nums):
    head, *tails = nums
    return head + sum(tails) if tails else head


def search(lines, partten, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if partten in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    base_path = '/Users/beast/PycharmProjects/python_cookbook'
    with timer('text drop first and last function'):
        grades = range(0, 5)
        res = drop_first_last(grades)
        print(res)

    with timer('text * expression'):
        records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4)
        ]

        for tag, *args in records:
            if tag == 'foo':
                do_foo(*args)
            elif tag == 'bar':
                do_bar(*args)

    with timer('test * expression in split string'):
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        uname, *fileds, homedir, sh = line.strip().split(':')
        print(f'uname is: {uname}\n'
              f'homedir is: {homedir}\n'
              f'sh is: {sh}')

    with timer('test deque'):
        with open(base_path + '/datasets/demo_deque', 'r', encoding='utf-8') as f:
            for line, previous_lines in search(f, 'python', 5):
                for pline in previous_lines:
                    print(pline, end=' ')
                print(line, end=' ')
                print('-' * 20)

