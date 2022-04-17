# 时间：2021年3月10日18:30:52
# 功能：
# 目的：
import math


def a(*args):
    print(*args)


x = 0.5
y = 2
a(math.sin(x))
a(math.cos(x))
a(math.asin(x))
a(math.acos(x))
a(math.tan(x))
a(math.atan(x))  # 加a的属于反三角函数
a(math.hypot(x, y))  # 求三角形斜边
a(math.fmod(x, y))  # 求x/y的余数相当于%
a(math.ceil(x))  # 取不小于x的最小整数
a(math.floor(x))  # 同上，单数取最小整数
a(math.fabs(x))  # 绝对值
a(math.exp(2))  # 求e的x次方
a(math.pow(x, y))  # 求x的y次幂
a(math.log10(23))  # 求x的10底对数
a(math.sqrt(y))  # 求x的平方根
a(math.pi)  # π的值


# 在python中运行的结果是：
# 总结：
