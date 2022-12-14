# 时间：2021年2月2日10:55:18
# 功能：求5位数的水仙花数
# 目的：算法理解
import math as u
# 代码1：
for item in range(1000, 10000):
    a = item//1000  # 取个位
    b = item//10 % 10  # 取十位
    c = item//100 % 10  # 取百位
    d = item % 10  # 取千位
    if item == a**4+b**4+c**4+d**4:
        print('水仙数为', item)
# 缺点：代码太长

# 代码2：

for i in range(1000, 10000):
    if u.pow((i//1000), 4)+u.pow((i//10 % 10), 4)+u.pow((i//100 % 10), 4)+u.pow((i % 10), 4) == i:
        print('水仙花数为', i)

# 可读性质一般

# 在python中运行的结果是：
# 水仙数为 1634
# 水仙数为 8208
# 水仙数为 9474
# 水仙花数为 1634
# 水仙花数为 8208
# 水仙花数为 9474
# 总结：模块的别名不能与变量名字重复
