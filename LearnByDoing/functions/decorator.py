import functools
"""
    functools.wraps: 需要把原始函数的__name__等属性复制到wrapper()函数中，
    否则，有些依赖函数签名的代码执行就会出错
"""

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log_text(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_text(u'我们开始吧')
def now():
    print(u'有一天，就是今天，今天就是有一天')


if __name__ == '__main__':
    print(now)
    now()
    print(now.__name__)

