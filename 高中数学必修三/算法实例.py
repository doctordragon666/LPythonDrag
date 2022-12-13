# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#

def get_factor1(m, n):
    """辗转相除法"""
    r = 1
    while r != 0:
        r = m % n
        m = n
        n = r
    return m

def get_factor2(m,n):
    return m-n

strings = 'i,sb,sd'
lst = strings.split(',')
print(lst)

# 运行结果
