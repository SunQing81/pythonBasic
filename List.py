# 创建列表，通过[]来创建列表
my_list = []
print(my_list, type(my_list))
# 列表存储的数据，我们称为元素
# 一个列表可以存储多个元素，也可以在创建列表时，来指定列表中的元素
my_list = [10]  # 创建只有一个元素的列表
# 当向列表中添加多个元素时，使用,隔开,可以保存任意的对象

my_list = [10, 20, 'hello', [1, 2], print]

print(my_list)

# 列表中的对象按照插入顺序存储到列表中
# 通过索引（index）来获取列表中的元素
# 索引从0开始
# 语法：list[索引值]
print(my_list[2])
# 超出索引值会抛出异常
# print(my_list[5]) IndexError: list index out of range

# 获取列表长度，即列表中元素的个数
# len()函数用来获取列表长度
print(len(my_list))

str_list = ['h', 'e', 'l', 'l', 'o']
string = 'hello'
print(str_list[-1])
print(str_list[0:3])  # 包前不包尾
print(str_list[::2])  # 包前不包尾
print(str_list[::-2])  # 包前不包尾
print(string[-1])

str_list = ['h', 'e', 'l', 'l', 'o']
int_list = [1, 2, 3]
print(str_list + int_list)
print(int_list * 3)

str_list = ['h', 'e', 'l', 'l', 'o']
print('o' in str_list)
print('o' not in str_list)

int_list = [1, 2, 3]
print('列表最大值:', max(int_list), '列表最小值：', min(int_list))

str_list = ['h', 'e', 'l', 'l', 'o']
print(str_list.index('l'))
print(str_list.index('l', 3, 6))
print(str_list.count('l'))

string = 'hello'
print('l' in string)

string = '123'
print(max(string))

str_list = ['h', 'e', 'l', 'l', 'o']
str_list[0:1] = '123'
print(str_list)
