a = int(10)
b = str('hello')
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>


class MyClass:
    pass


print(MyClass)  # <class '__main__.MyClass'>
# 使用类来创建对象，就像调用一个函数一样
myClass = MyClass()
print(myClass)  # <__main__.MyClass object at 0x0000025DD6054FD0>
myClass02 = MyClass()
myClass03 = MyClass()
myClass04 = MyClass()
# isinstance() 函数用来检查一个对象是否是一个类的实例
result = isinstance(myClass, MyClass)
print(result)  # True
print(type(MyClass))  # <class 'type'>
