from utils.time_utils import *
from collections import namedtuple


def compute_cost(records):
    total = 0.0
    for record in records:
        total += record[1] * record[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'prices'])


def compute_cost_namedtuple(records):
    total = 0.0
    for record in records:
        s = Stock(*record)
        total += s.prices * s.shares
    return total


if __name__ == '__main__':
    with timer('test namedtuple'):
        Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
        sub = Subscriber('jonesy@example.com', '2012-10-19')
        len = len(sub)
        addr, joined = sub
        print(f'object is: {sub}\n'
              f'addr is: {sub.addr}\n'
              f'joined is: {sub.joined}\n'
              f'length of sub is: {len}\n'
              f'addr is {addr}\n'
              f'joined is: {joined}')
