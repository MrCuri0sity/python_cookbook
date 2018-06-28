def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib_gene(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def triangles(number):
    a, n = [1], 0
    while n < number:
        yield a
        a = [sum(i) for i in zip(a + [0], [0] + a)]
        n = n + 1
    return 'done'





if __name__ == '__main__':
    print(fib(6))
    G = fib_gene(6)
    while True:
        try:
            x = next(G)
            print(f'g: {x}')
        except StopIteration as e:
            print(f'Generator return value: {e.value}')
            break

    G_t = triangles(10)
    while True:
        try:
            x = next(G_t)
            print(x)
        except StopIteration as e:
            print(f'Generator return value: {e.value}')
            break
