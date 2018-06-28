from utils.time_utils import *
from operator import attrgetter

class User:
    def __init__(self, userId):
        self.userId = userId

    def __repr__(self):
        return 'User({})'.format(self.userId)


if __name__ == '__main__':
    with timer('test attrgetter'):
        users = [User(23), User(3), User(99)]
        sorted_lambda = sorted(users, key=lambda u: u.userId)
        sorted_attrgetter = sorted(users, key=attrgetter('userId'))
        print(f'sort by lambda function is: {sorted_lambda}\n'
              f'sort by attrgetter is: {sorted_attrgetter}')
        min_user = min(users, key=attrgetter('userId'))
        max_user = max(users, key=attrgetter('userId'))
        print(f'min userId is: {min_user}\n'
              f'max userId is: {max_user}')
