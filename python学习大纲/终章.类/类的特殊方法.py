# 时间：2021年2月21日16:16:02
# 功能:python编译器的方法
# 目的：

# 特殊的属性
# 遍历所有的类属性
for attribute in dir(object):
    print(attribute)
print('-----------------')

# __dict__表示将实例对象(也可以是类名)所有的属性以字典形式输出
for key, value in object.__dict__.items():
    print(key, " ", value)

a = object
print(a.__class__)  # 输出对象所属的类
print(a.__bases__)  # 输出的是父类类型的元素,不加s只会输出第一个
print(a.__mro__)  # 类的层次结构
print(a.__subclasses__)  # 所有的子类列表

# 特殊的方法,使得将一些操作可以在类中实现
a = 13
b = 145
print(a.__add__(b))  # python将+作为一个对象方法


class Fun (object):
    # __init__后被调用，因为他是对新创建一个对象进行初始化
    def __init__(self, name):
        print('将父类创造的对象实例化')
        self.name = name

    def __add__(self, other):
        return self.name + other.name  # 重载运算符

    # 将len的作用扩大，使之可以判断字符的长度
    def __len__(self):
        return len(self.name)

    # 这是new方法的特点，他会被最先调用，因为这是继承
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('系统的自动构造一个空对象')
        ig = super().__new__(cls)
        return ig


a = Fun('individual')
b = Fun('tedious')
print(a+b, len(a), a.name)

# 在python中运行的结果是：
# 总结：
