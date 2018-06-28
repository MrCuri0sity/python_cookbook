from utils.time_utils import *
from operator import itemgetter


if __name__ == '__main__':
    with timer('test itemgetter'):
        rows = [
            {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
            {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
            {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]
        rows_by_fname = sorted(rows, key=itemgetter('fname'))
        rows_by_uid = sorted(rows, key=itemgetter('uid'))
        rows_by_flname = sorted(rows, key=itemgetter('lname', 'fname'))
        print(f'sort by fname is: {rows_by_fname}\n'
              f'sort by uid is: {rows_by_uid}\n'
              f'sort by fname and lname is: {rows_by_flname}')
        min_by_fname = min(rows, key=itemgetter('fname'))
        max_by_uid = max(rows, key=itemgetter('uid'))
        print(f'min fname is: {min_by_fname}\n'
              f'max uid is: {max_by_uid}')
