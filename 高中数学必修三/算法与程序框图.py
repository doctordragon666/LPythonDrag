# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
import math

chapter_line = '-----------\n'


def get_root(equal1, equal2):
    # 1.求解二元一次方程组
    # equal1 = input("请输入第一个方程组的参数,用逗号分开")
    [a1, b1, c1] = map(lambda x: int(x), equal1.split(','))
    # equal2 = input("请输入第二个方程组的参数，用逗号分开")
    [a2, b2, c2] = map(lambda x: int(x), equal2.split(','))
    """暂时不考虑为0的情况，因为教材上也没有考虑"""
    rootx = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
    rooty = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
    print(f"x={rootx}, y={rooty}", end=chapter_line)
    return rootx, rooty


def is_prime(num):
    # 2.判断一个数是否为质数
    if num < 2:
        print("教材要求数字必须大于2")
        return False
    else:
        i = 2
        while i < num:
            if num % i == 0:
                print(f"num{num} is not prime", end=chapter_line)
                return False
            i += 1
        print(f"num{num} is a prime", end=chapter_line)
        return True


def fun(x):
    return pow(x, 2) - 2


def get_estimate():
    # 3.二分法求方程近似解
    left = 1
    right = 2
    precise = 0.005
    while right - left > precise:
        mid = (left + right) / 2
        if fun(mid) * fun(left) < 0:
            right = mid
        else:
            left = mid
    print(f"the solution result is in [{left}, {right}]", end=chapter_line)
    return left, right


def get_triangle_area(a, b, c):
    # 4. 使用海伦公式
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def is_triangle(a, b, c):
    # 5.判断是否为三角形
    return a + b > c and a + c > b and b + c > a


def get_array_sum():
    return sum(range(1, 101))


def get_year():
    n = 2005
    a = 200
    while a <= 300:
        t = 0.05 * a
        a += t
        n += 1
    return n

# 运行结果
