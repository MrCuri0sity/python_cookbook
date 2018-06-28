def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


if __name__ == '__main__':
    f1, f2, f3 = count()
    print(f'{f1}\n{f2}\n{f3}\n')
    print('=' * 60)
    print(f'{f1()}\n{f2()}\n{f3()}\n')
    """
        全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
        等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
    """
    """
        返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    """
    f1, f2, f3 = count1()
    print(f'{f1}\n{f2}\n{f3}\n')
    print('=' * 60)
    print(f'{f1()}\n{f2()}\n{f3()}\n')