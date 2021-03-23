# if True:
#     print(123)
#     print(456)
#     print(789)
# print("if管不了")

# a = input('请输入：')
# print('输入的内容是：', a)
#
# i = 0
# while i < 10:
#     i += 1
#     print(i, 'hello world')
# else:
#     print('循环结束')

# 1000以内水仙花练习题
# i = 100
# while i < 1000:
#     hundred = i // 100
    # ten = i // 10 % 10
    # ten = (i - hundred * 100) // 10
    # one = i % 10
    # print(i,hundred,ten,one)

    # if hundred ** 3 + ten ** 3 + one ** 3 == i:
    #     print(i, "是水仙花数")
    # i += 1

# 判断输入的数是否为质数
# num = int(input('输入任意数:'))
# i = 2
# flag = True
# while i < num:
#     if num % i == 0:
#         flag = False
#         break
#     i += 1
# if flag:
#     print(num, '是质数')
# else:
#     print(num, '不是质数')



# 倒直角三角形

# i = 0
# while i < 5:
#     j = 0
#     while j < 5 - i:
#         print('* ',end='')
#         j += 1
#     print()
#     i += 1
#
# print('=========================================================')

# 九九乘法表
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(j,'*',i,'=',i*j,end=' ')
#         j += 1
#     print()
#     i += 1
#
# print('=========================================================')
from time import *
begin = time()
# 100以内的所有质数
i = 2
count = 0
while i < 100000:
    flag = True
    j = 2
    while j <= i ** 0.5:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        count += 1
        print(i,end=' ')
        if count % 5 == 0: print()
    i += 1
end = time()
print('程序运行时间为',end - begin,'秒')
# 0.007957935333251953   0.0019795894622802734