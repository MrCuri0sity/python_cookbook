from utils.time_utils import *

if __name__ == '__main__':
    with timer('test options with slice object'):
        items = [0, 1, 2, 3, 4, 5, 6]
        a = slice(2, 4)
        print(f'get slice: {items[2: 4]}\n'
              f'get slice use slice object: {items[a]}\n')
        print(f'raw items is: {items}')
        items[a] = [10, 11]
        print(f'replace items is: {items}')
        del items[a]
        print(f'del items is: {items}')
        a = slice(5, 50, 2)
        print(f'a.start is: {a.start}\n'
              f'a.end is: {a.stop}\n'
              f'a.step is: {a.step}')
        """
            indices(size) 方法将它映射到一个已知大小的序列上
        """
        s = 'HelloWorld'
        a_indices = a.indices(len(s))
        print(f'a_indices is: {a.indices(len(s))}')
        # print(f'a.start is: {a_indices.start}\n'
        #       f'a.end is: {a_indices.stop}\n'
        #       f'a.step is: {a_indices.step}')
        for i in range(*a.indices(len(s))):
            print(s[i])

