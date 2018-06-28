from utils.time_utils import *

if __name__ == '__main__':
    with timer('test zip when sort dict'):
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        print('use zip to get key and value')
        max_price = max(zip(prices.values(), prices.keys()))
        min_price = min(zip(prices.values(), prices.keys()))
        sorted_prices = sorted(zip(prices.values(), prices.keys()), reverse=True)
        print(f'max price is: {max_price}\n'
              f'min price is: {min_price}\n'
              f'sorted prices is: {sorted_prices}')

    with timer('test dict set options'):
        a = {
            'x': 1,
            'y': 2,
            'z': 3
        }

        b = {
            'w': 10,
            'x': 11,
            'y': 2
        }
        keys_common = a.keys() & b.keys()
        keys_complement = a.keys() - b.keys()
        print(a.keys())
        print(a.values())
        # values_common = a.values() & b.values()
        items_common = a.items() & b.items()
        print(f'keys in common is: {keys_common}\n'
              # f'values in common is: {values_common}\n'
              f'items in common is: {items_common}\n'
              f'the complementary between a and b is {keys_complement}')

    with timer('method 1 take a subset of dict'):
        """
            字典推导
        """
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        # Make a dictionary of all prices over 200
        p1 = {key: value for key, value in prices.items() if value > 200}
        # Make a dictionary of tech stocks
        tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
        p2 = {key: value for key, value in prices.items() if key in tech_names}
        print(f'p1 is: {p1}\n'
              f'p2 is: {p2}')
        """
            创建tuple然后传给dict()
        """
    with timer('method 2: take a subset of dict'):
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
        p1_dict = dict((key, value) for key, value in prices.items() if value > 200)
        p2_dict = dict((key, value) for key, value in prices.items() if value in tech_names)
        print(f'p1 is: {p1}\n'
              f'p2 is: {p2}')