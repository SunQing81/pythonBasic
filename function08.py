l = [1, '2', '34', 4, 5, 6, 7, 8]
l.sort(key=int)
print(l)  # [1, '2', 4, 5, 6, 7, 8, '34']
l.sort(key=str)
print(l)  # [1, '2', '34', 4, 5, 6, 7, 8]
l = [1, '2', '34', 4, 5, 6, 7, 8]
print('修改后的列表是：', sorted(l, key=int))  # [1, '2', 4, 5, 6, 7, 8, '34']
print('原列表是：', l)  # [1, '2', '34', 4, 5, 6, 7, 8]


def external():
    nums = []

    def averageNum(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return averageNum


averageNum = external()
print(averageNum(2))  # 2.0
print(averageNum(3))  # 2.5
print(averageNum(5))  # 3.3333333333333335
print(averageNum(5))  # 3.75
