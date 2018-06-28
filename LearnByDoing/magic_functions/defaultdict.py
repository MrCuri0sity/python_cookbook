from collections import defaultdict
from utils.time_utils import *

if __name__ == '__main__':
    with timer('test defaultdict'):
        d_list = defaultdict(list)
        d_list['a'].append(1)
        d_list['a'].append(2)
        d_list['a'].append(2)
        d_list['b'].append(3)

        d_set = defaultdict(set)
        d_set['a'].add(1)
        d_set['a'].add(2)
        d_set['a'].add(1)
        d_set['b'].add(2)

        print(f'd_list: {d_list}\n'
              f'd_set: {d_set}')