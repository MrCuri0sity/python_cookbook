from utils.time_utils import *
from itertools import compress

if __name__ == '__main__':
    with timer('test compress'):
        addresses = [
            '5412 N CLARK',
            '5148 N CLARK',
            '5800 E 58TH',
            '2122 N CLARK',
            '5645 N RAVENSWOOD',
            '1060 W ADDISON',
            '4801 N BROADWAY',
            '1039 W GRANVILLE',
        ]
        counts = [0, 3, 10, 4, 1, 7, 6, 1]
        more5 = [n > 5 for n in counts]
        more5_address = list(compress(addresses, more5))
        print(f'more than 5 is: {more5_address}')