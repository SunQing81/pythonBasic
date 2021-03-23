a = [2, 4, 5, 6]
b = [2, 4, 5, 6]
print(id(a) == id(b))  # False
print(a == b)  # True
b = a
print(a is b)  # True
