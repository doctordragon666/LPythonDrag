# 时间：2021年3月11日20:16:11
# 功能：
# 目的：

def sun(*args):
    return sum(args)


s = lambda x, y, z: (sun(x, y, z))
print(s(1, 2, 3), type(s))
"""
格式：lambda params:expr
params表示函数参数列表中的参数
expr函数要返回值的表达式，不能含有其他的语句
可以返回元组（要括号），允许调用其他函数
"""

lst = [1, 23, 34, 5]
help(abs)  # 显示对象的帮助信息，输入函数名字即可，相当于按下ctrl
print(bin(12), hex(12), oct(12))  # 二进制，八进制，十六进制
print(callable(sun))  # 测试对象是否可调用
print(chr(78))  # 将ASCII转化为字符
lst2 = list(filter(lambda x: x < 1, lst))  # filter 用函数过滤数据中符合函数的数据
lst3 = list(map(lambda x: x*2, lst))  # map 对列表（其他类型也可）中的元素进行变化
lst = list(map(lambda x: x*2, lst))
if isinstance(sun, str):
    print('正确')
else:
    print('正确的数据类型为', type(sun))
for z in lst3:
    print(z)
print('------------------')
for i in lst2:
    print(i)
# 在python中运行的结果是：
# 总结：
