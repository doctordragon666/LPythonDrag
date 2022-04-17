# -*- coding:utf-8 -*-
# 时间：2021年3月24日21:53:08
# 功能：计算圆的面积和周长
# 目的：使用类创造出一个圆
import math as x


class Circle(object):
    def __init__(self, r=0.0, pi=x.pi):
        self.r = r
        self.pi = pi

    def info(self):
        print(f"圆的面积为{self.r**2*self.pi}")
        print(f"圆的周长为{self.r*2*self.pi}")


pi1 = float(input('请输入π的值（不输入默认为3.141592653589793）'))
r1 = float(input('请输入半径'))
Circle(r1, pi1).info()
# 在python中运行的结果是：
# 请输入π的值（不输入默认为3.14）3.1415926
# 请输入半径1
# 圆的周长为 6.2831852
# 圆的面积为 3.1415926
# 总结：字符串的转化很重要
