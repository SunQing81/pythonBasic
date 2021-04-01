# 练习1 求任意数的幂运算
def power(n: int, i: int) -> int:
    """
    为任意数字做幂运算
    :param n: 底数
    :param i: 指数
    :return: 幂运算的结果
    """
    if i == 1:
        return n
    else:
        return n * power(n, i - 1)


result = power(2, 3)
print(result)


def palindromeStr(str):
    """
    判断str是否是回文字符串:len(str) - 1 == -1
    :param str:
    :return:
    """
    if len(str) < 2:
        return "是回文字符串"
    elif str[0] != str[-1]:
        return '不是回文字符串'
    return palindromeStr(str[1:-1])


print(palindromeStr('abxxsba'))
