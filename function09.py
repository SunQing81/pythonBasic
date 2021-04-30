def begin_end(old):
    """
    用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行
    执行后打印执行结束
    :param old: 要扩展的函数对象
    :return: 返回一个新的函数
    """

    def new_function(*agrs, **kwargs):
        print('begin_end开始执行。。。')
        result = old(*agrs, **kwargs)
        print('begin_end执行结束。。。')
        return result

    # 返回一个新的函数
    return new_function


def begin_end02(old):
    """
    用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行
    执行后打印执行结束
    :param old: 要扩展的函数对象
    :return: 返回一个新的函数
    """

    def new_function(*agrs, **kwargs):
        print('begin_end02开始执行。。。')
        result = old(*agrs, **kwargs)
        print('begin_end02执行结束。。。')
        return result

    # 返回一个新的函数
    return new_function


def printtest():
    return '输出测试'


def sum(a, b):
    return a + b


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


new_fun = begin_end(sum)
print(new_fun(1, 2))

new_fun = begin_end(factorial)
print(new_fun(2))


# 通过@装饰器来装饰函数
@begin_end
def test():
    print('nihaoa')


test()


@begin_end
@begin_end02
def test2():
    print('两个装饰器实例')
test2()