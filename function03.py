def fn():
    # return 'hello'
    # return [1, 2, 3]
    # return {'k': 3}
    #
    def fn2():
        print('fn2')

    return fn2


r = fn()  # 函数的返回值就是他的结果
r()
print(r)
