# 定义一个人的类
class Person:
    # name = 'tony'  # 保存在类中,是固定的，
    # 可以当作参数传递
    # 使用类创建对象时，类后面的所有参数都会依次传递到init()中
    def __init__(self, name):
        print('init方法被调用')
        # name属性保存在对象中
        self.name = name

    # 第一个参数就是调用方法的对象本身
    # 一般我们会将这个参数命名为self
    def eat(self):
        # 若实例中未定义name属性时，调用此方法会报错
        print(self.name, '你妈妈喊你吃饭')


p1 = Person('jack')
p2 = Person('tom')
p3 = Person('tony')
p1.eat()
p2.eat()
p3.eat()


# 练习 1 狗
class Dog:
    def __init__(self, name):
        self.hidden_name = name

    def getName(self):
        print(self.hidden_name)

    def setName(self, name):
        self.hidden_name = name

    def jiao(self):
        """
        狗叫
        :return:
        """
        print(self.hidden_name, '汪汪汪')


d1 = Dog('旺财')
d1.getName()
d1.setName('小黑')
d1.getName()


# 练习2 面积
class Rectangle:
    def __init__(self, long, width):
        self.hidden_long = long
        self.hidden_width = width

    def getLong(self):
        return self.hidden_long

    def setLong(self, long):
        self.hidden_long = long

    def getWidth(self):
        return self.hidden_width

    def setWidth(self, width):
        self.hidden_width = width

    def getArea(self):
        return self.hidden_long * self.hidden_width


r1 = Rectangle(2, 5)
print(r1.getArea())
r1.setWidth(7)
print(r1.getArea())
