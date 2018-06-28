def fact(n):
    """
    calculate fact use recursive
    :param n:
    :return:
    """
    assert(n > 0), 'input n should be a positive number, while input is {}'.format(n)
    assert(isinstance(n, int)), 'input n should be integer, while input n is ({0})'.format(type(n))
    if n == 1:
        return 1
    return fact(n-1) * n


if __name__ == '__main__':
    print(fact(3))