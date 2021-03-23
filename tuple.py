# my_tuple = ()  # 创建一个空元组
# print(my_tuple, type(my_tuple))  # () <class 'tuple'>
#
# my_tuple = (1, 2, 3, 4, 5)  # 创建一个有五个元素的元组
# print(my_tuple)

# my_tuple[0] = 1  # TypeError: 'tuple' object does not support item(项目) assignment(任务)
# print(my_tuple[0])
#
# my_tuple = 10, 20
# print(my_tuple)
#
# my_tuple = 10,
# print(my_tuple)

# my_tuple = 1, 2, 3, 4
# a, b, c, d = my_tuple
# print('a =', a)  # a = 1
# print('b =', b)  # b = 2
# print('c =', c)  # c = 3
# print('d =', d)  # d = 4

# a, b = my_tuple # ValueError: too many values to unpack (expected 2)
# a, b, *c = my_tuple
# print('a =', a)  # a = 1
# print('b =', b)  # b = 2
# print('c =', c)  # c = [3, 4]
#
# a, *b, c = my_tuple
# print('a =', a)  # a = 1
# print('b =', b)  # b = [2, 3]
# print('c =', c)  # c = 4
#
# *a, b, c = my_tuple
# print('a =', a)  # a = [1, 2]
# print('b =', b)  # b = 3
# print('c =', c)  # c = 4

# *a, *b, c = my_tuple  # SyntaxError: multiple starred expressions in assignment

my_list = [1, 2, 3, 4]
a, b, *c = my_list
print('a =', a)  # a = 1
print('b =', b)  # b = 2
print('c =', c)  # c = [3, 4]

my_str = 'hello'
*a, b, c = my_str
print('a =', a)  # a = [h, e, l]
print('b =', b)  # b = l
print('c =', c)  # c = o
# a = 100
# b = 200
# a, b = b, a
# print('a =', a)  # a = 200
# print('b =', b)  # b = 100


