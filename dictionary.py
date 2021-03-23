# 字典
d = {}  # 空字典
d = {'name': "猴子", 'age': 525, 'gender': 'man'}
print(d, type(d))
print(d['name'], d['age'])
# print(d['address'])  # KeyError: 'address'
d = dict(name='猴子', age=544, gender='man')
print(d, type(d))  # {'name': '猴子', 'age': 544, 'gender': 'man'} <class 'dict'>
d = dict([(1, 2), (3, 4)])
print(d, type(d))  # {1: 2, 3: 4} <class 'dict'>
