# 高阶函数
#  接受一个或多个函数作为参数或将函数作为返回值返回


def getDoubleNum(i):
    """
    判断一个数是否为偶数
    :param i: 任意数
    :return: true false
    """
    if i % 2 == 0:
        return True
    return False


l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(getDoubleNum, l)))  # [2, 4, 6, 8]


def getExceedNum(i):
    """
    判断输入的数据是否大于某个数
    :param i: 输入的数
    :return: true false
    """
    if i > 5:
        return True
    return False


def getNewListByFun(fun, initList):
    """
    根据传入的函数规则，来获取新规则下的列表
    :param fun: 传入的函数
    :param initList: 初始列表
    :return: 返回一个新的列表
    """
    newList = []
    for n in initList:
        if fun(n):
            newList.append(n)

    return newList


print(getNewListByFun(getDoubleNum, l))
print(getNewListByFun(getExceedNum, l))


def sum(a, b):
    return a + b


# 等价于
lambda a, b: a + b

# lambda调用方式
print((lambda a, b: a + b)(1, 2))
# 也可以赋值给一个变量，通过调用变量来执行函数
var = lambda a, b: a + b
print(var(2, 4))
# 主要用处
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(lambda i: i % 2 == 0, l)))  # [2, 4, 6, 8]

# map() 函数
# 对指定的可迭代对象操作，返回一个新的对象
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda i: i ** 2, l)))
