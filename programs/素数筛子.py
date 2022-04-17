# -*- coding:utf-8 -*-
# 时间：2021年5月6日10:51:21
# 功能：随机获取该范围内的若干个素数
# 目的：
import random

"""求素数"""
i = int(input('输入所求的范围'))
lst = []
for _ in range(2, i):
    val = 2
    while val < _:
        if _ % val == 0:
            break
        val += 1
    if val == _:
        lst.append(_)
    else:
        continue
"""随机取两个数"""
for a,b in enumerate(lst):  # 将lst的下标和值一起遍历
    if a == int(len(lst)*random.random()):
        print(a, b)
# 在python中运行的结果是：
# 总结：
