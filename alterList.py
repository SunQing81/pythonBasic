str_list = ['h', 'e', 'l', 'l', 'o']
# 通过索引值修改列表元素
str_list[0] = 'n'
print(str_list)  # ['n', 'e', 'l', 'l', 'o']
# 通过切片修改列表元素
str_list[0:1] = ['h']  # 在给切片赋值时，只能使用序列
print(str_list)  # ['h', 'e', 'l', 'l', 'o']
# 在索引值为0处添加元素
str_list[0:0] = ['h', 'i']
print(str_list)  # ['h', 'i', 'h', 'e', 'l', 'l', 'o']
# 当设置步长时，切片序列的元素与原列表的元素个数一致
str_list[::3] = ['l', 'i', 'l']
print(str_list)  # ['l', 'i', 'h', 'i', 'l', 'l', 'l']
# 通过切片删除
str_list[4:] = []
print(str_list)  # ['l', 'i', 'h', 'i']

# append()
# myList = [0, 1, 2, 3]
# print('原列表：', myList)  # 原列表： [0, 1, 2, 3]
# myList.append(4)
# print('修改后：', myList)  # 修改后： [0, 1, 2, 3, 4]
# insert()
# myList.insert(2, 5)
# print('修改后：', myList)  # 修改后： [0, 1, 5, 2, 3]
# extend()
# myList.extend(['1', '2', '3'])
# myList += ['1', '2', '3']
# print('修改后：', myList)  # 修改后： [0, 1, 2, 3, '1', '2', '3']

myList = [0, 1, 2, 3]
# print('原列表：', myList)  # 原列表： [0, 1, 2, 3]
# clear():清空列表
# myList.clear()
# print('修改后：', myList)  # 修改后： []
# pop():有参数--删除指定索引位置的元素；无参--删除最后一个元素
# myList.pop(2)
# print('修改后：', myList)  # 修改后： [0, 1, 3]
# myList.pop()
# print('修改后：', myList)  # 修改后： [0, 1, 2]
# remove():删除指定元素，若含有多个相同参数，则删除第一个
# myList.remove(3)
# print('修改后：', myList)  # 修改后： [0, 1, 2]
# myList.append(3)
# print('元素增加', myList)  # 元素增加 [0, 1, 2, 3, 3]
# myList.remove(3)
# print('修改后：', myList)  # 修改后： [0, 1, 2, 3]

# reverse()
# myList.reverse()
# print('修改后：', myList)  # 修改后： [3, 2, 1, 0]

# sort()
# myList = list('4235463')
# print('原列表：', myList)  # 原列表： ['4', '2', '3', '5', '4', '6', '3']
# myList.sort()
# print('修改后：', myList)  # 修改后： ['2', '3', '3', '4', '4', '5', '6']
# myList.sort(reverse=True)
# print('修改后：', myList)  # 修改后： ['6', '5', '4', '4', '3', '3', '2']

# 遍历列表
# for循环
myList = [0, 1, 2, 3]
for i in myList:
    print(i, end=' ')  # 0 1 2 3
