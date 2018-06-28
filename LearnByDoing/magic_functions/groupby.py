from itertools import groupby
from operator import itemgetter
from utils.time_utils import *
from collections import defaultdict

if __name__ == '__main__':
    with timer('test groupby'):
        rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]
        """
            groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。
        """
        rows.sort(key=itemgetter('date'))
        for date, items in groupby(rows, key=itemgetter('date')):
            print(date)
            for item in items:
                print(' ', item)

        row_by_date = defaultdict(list)
        for row in rows:
            row_by_date[row['date']].append(row)

        for r in row_by_date['07/01/2012']:
            print(r)