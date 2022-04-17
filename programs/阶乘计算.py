# 时间：2021年3月1日09:20:10
# 功能：计算阶乘
# 目的：
import os


def word():
    """求阶乘"""
    y = int(input("请输入你想求的阶乘数字"))
    x = 1
    for _ in range(1, y):
        x *= _
    print(y, '的阶乘为', x)


if __name__ == '__main__':
    while True:
        word()
        z = input('你想继续运行吗？y/n')
        if z == 'y':
            i = os.system('cls')
            word()
        else:
            break

# 在python中运行的结果是：
# 总结：
