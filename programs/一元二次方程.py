# -*- coding:utf-8 -*-
# 时间：2021年3月20日21:11:55
# 功能：
# 目的：
import math


def fun(num):
    return 1 if num-int(num) == 0 else 0


def way1(p, q, date):  # 处理小数为0的情况
    i = math.sqrt(date)
    x1 = (-q+i)/2*p
    x2 = (-q-i)/2*p
    if fun(x1) and fun(x2):  # 判断是否为整数
        if date == 0:
            print("该方程有两个相同的解为", x1)
        else:
            print("该方程的二个解为", x1, x2)
    else:
        r1, r2, r3 = str((-q+i)), str((-q-i)), str((2*p))
        root1 = r1 + '/' + r3
        root2 = r2 + '/' + r3
        if date == 0:
            print('该方程有两个相同的解为'+root1)
        else:
            print('该方程的二个解为'+root1+root2)


def way2(p, q, date):  # 当小数不为0时，需要将其保留根号
    date1 = str(date)
    i = '+根号'+date1
    r1, r2, r3 = (str(-q) + i), (str(-q) + '-' + i), str((2 * p))
    root1 = '('+r1 + ')' + '/' + r3
    root2 = '('+r2 + ')' + '/' + r3
    if date == 0:
        print('该方程有两个相同的解为' + root1)
    else:
        print('该方程的二个解为:x1={0},x2={1}'.format(root1, root2))


while True:
    print('欢迎使用一元二次方程求解系统')
    a = int(input('请输入方程的二次项系数'))
    b = int(input('请输入方程的一次项系数'))
    c = int(input('请输入方程的常数'))
    if a == 0:
        print('此方程仅有唯一解，解为', -c/b)
        continue  # 确定其为一元二次方程
    data = b**2 - 4*a*c  # 初始化判别式
    if data < 0:
        print('此方程无实数解')
        break
    if fun(math.sqrt(data)):
        way1(a, b, data)  # 运用计算机运算能力
    else:
        way2(a, b, data)  # 使用字符串拼接，根据实际需要来进行赋值
    answer = input('你想继续吗？ yes/no')  # 人机交互环节
    if answer == 'yes':
        continue
    else:
        break

# 在python中运行的结果是：
# 总结：
