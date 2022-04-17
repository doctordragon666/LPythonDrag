# 时间：2021年2月19日14:55:52
# 功能：
# 目的：继承与多态

# 继承
import abc


class FUN1(object):
    def __init__(self, name, old):
        self.Na = name
        self.__y = old  # RR通过加两条下划线，可以防止该数据被访问

    def printf(self):
        print(self.Na, self.__y)

    def get_old(self):
        return self.__y


class FUN2(FUN1):
    def __init__(self, name, old, card):
        super().__init__(name, old)
        super().printf()
        self.p = card


Q = FUN2('JIANG', 23, 43546)
Q.printf()
print(Q.Na)
print(Q.p)

# 封装:见RR处,将部分函数的数据进行封装
print(dir(FUN1))  # 打开该类的所有目录
# print(Q.__y) # 无法运行，因为你已经设定他无法访问。tips:版本低的可以访问，但是该版本不行

# 多态
'''
对于同一父类的对象，无论传入什么参数，都能做出一致的反应
'''


class Animal(object):
    @abc.abstractmethod
    def eat(self):
        pass  # 纯虚类


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Cow(Animal):
    def eat(self):
        print('牛吃草')


class Person(Animal):
    def eat(self):
        print('茹毛饮血')


def fun(obj):
    obj.eat()  # 传入一个对象，调用对象的方法


fun(Cat())
fun(Cow())
# 在python中运行的结果是：
# 总结：
