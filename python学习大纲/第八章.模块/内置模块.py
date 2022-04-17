# 时间：2021年2月22日15:30:02
# 功能：
# 目的：
import sys
import time
import calendar
import urllib.request
import json
import re
import decimal
import logging
import random

'''
sys
与Python解释器及其环境操作相关的标准库
time
提供与时间相关的各种函数的标准库
os
提供了访问操作系统服务功能的标准库
calendar
提供与日期相关的各种函数的标准库
ur1lib
用于读取来自网上（服务器）的数据标准库
json
用于使用JSON序列化和反序列化对象
re
用于在字符串中执行正则表达式匹配和替换
math
提供标准算术运算函数的标准库
decimal
用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging提供了灵活的记录事件、错误、警告和调试信息等目志信息的功能
'''

print(sys.getsizeof(23), sys.getsizeof(False), '\n')  # 读取数据的大小
print(time.time(), '\n', time.localtime(time.time()), '\n')  # 查找当地时间。
# 注：w/y day 指的是一周(年)的第几天从0开始，is dst 指是否为夏令时，输出布尔值
print(random.random())  # 输出0~1之间的随机数
print(random.randint(0, 10))  # 生成0~10的随机整数
t = [2, 334, 45, 456, 656, 5, 7, 6]
print(random.choice(range(12)))
random.shuffle(t)  # 对列表的数据随机抽取元素，返回值为NONE

for _ in t:
    print(t)
'''
time.time()获取自初始时间至现在的秒数
datetime.datetime.now()获取本地的时间和日期
datetime.datetime.utcnow()获取当前的UTC日期/时期
'''

# print(urllib.request.urlopen('http://www.baidu.com').read())
# 爬取其中的相关内容
# 在python中运行的结果是：
# 总结：
