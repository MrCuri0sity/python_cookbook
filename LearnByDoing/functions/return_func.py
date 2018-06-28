def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = n + ax
        return ax
    return sum


def print_func(*args):
    print(args)


if __name__ == '__main__':
    f = lazy_sum(1, 2, 3)
    print_func(1, 2, 3)
    print(f)
    print(f())
