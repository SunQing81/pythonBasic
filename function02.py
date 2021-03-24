# 函数的参数
def sum(a, b):
    print(a, '+', b, '=', a + b)


sum(1, 2)
sum(234, 66)


# 设置形参默认值
def setDefaultParameter(a, b=2):
    print('a =', a, 'b =', b)


setDefaultParameter(1, 3)  # a = 1 b = 3
setDefaultParameter(1)  # a = 1 b = 2


# 不定长参数
def sumAnyParameter(*args):
    result = 0
    for n in args:
        result += n
    print(result)


sumAnyParameter()  # 0
sumAnyParameter(1, 2, 3, 4)  # 10


def test(*, a, b):
    print('a,b的值分别是', a, b)


test(a=1, b=2)  # a,b的值分别是 1 2


def test2(a, b, **c):
    print('a = ', a, 'b = ', b, 'c = ', c, 'c的类型是', type(c))


test2(1, b=2, c=3, d=4)  # a =  1 b =  2 c =  {'c': 3, 'd': 4} c的类型是 <class 'dict'>


# 练习1 求任意三个数的乘积
def multiply(a, b, c):
    print(a, '*', b, '*', c, '=', a * b * c)


multiply(1, 2, 3)


# 练习2 根据不同用户名显示不同信息
def showName(username):
    print('欢迎', username, '进入')


showName('zhangsan')
