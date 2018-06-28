import heapq
from utils.time_utils import *


class PriorityQueue:
    """
        implementation priority queue by heapq
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 为啥给priority加上负号
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    with timer('test heapq nlargest() and nsmallest()'):
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        print(f'3 largest number in nums is: {heapq.nlargest(3, nums)}\n'
              f'3 smallest number in nums is: {heapq.nsmallest(3, nums)}')
        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
        expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
        cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
        print(f'the most 3 expensive in portfolio is: {expensive}\n'
              f'the most 3 cheap in portfolio is: {cheap}')


