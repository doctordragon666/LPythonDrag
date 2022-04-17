# -*- coding:utf-8 -*-
# 日期：
# 功能：
# 目的：
import random


class Person(object):
    def __init__(self, name):
        self.name = name
        self.sex = ''
        self.birth = 2002

    def old(self):
        return 2020 - self.birth

    @staticmethod
    def talk(self):
        print('i am person')


class Kid(Person):
    def __init__(self):
        super(Kid, self).__init__(self)


class Rand:
    def __init__(self):
        pass

    def randoms(self):
        return random.random()


person1 = Person("liu")
rand1 = Rand().randoms()
print(rand1)
kid1 = Kid()
print(kid1.old())
lst = [12, 12]
lst.sort()
# 在python中运行的结果是：
# 总结：
