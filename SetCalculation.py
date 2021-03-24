# 再对集合做运算时，不会影响原来的集合，而是返回一个运算结果
# 创建两个集合
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
# & 交集运算
result = s & s2
print(result)  # {3, 4, 5}

# | 并集运算
result = s | s2
print(result)  # {1, 2, 3, 4, 5, 6, 7}

# - 差集
result = s - s2
print(result)  # {1, 2}

# ^ 异或集 获取只在一个集合中出现的元素
result = s ^ s2
print(result)  # {1, 2, 6, 7}

# <= 检查一个集合是否是另一个集合的子集
# 如果a集合中的元素全部都在b集合中出现，
# 那么a集合就是b集合的子集，b集合是a集合的超集
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
result = a <= b
print(result)  # True

# < 检查一个集合是否是另一个集合的真子集
# 即不包含其本身，少于本身元素的数量
result = a < b
print(result)  # True

# 还有 >= 和 > 这里不在重复
