# 时间：
# 功能：
# 目的：
# 局部和全局变量：局部变量出现在函数内部，全局变量定义在外部
def n():
    global a  # 可以使用global将局部变为全局，但是你需要引用一次函数
    a = 12
    print(a)


n()
print(a+12)
# 递归函数：占用的内存较大，内部一定要有if语句，否则会陷入死循环


def gui(b):
    if b > 23:
        return b
    else:
        return b * gui(b+1)


print(gui(1))

# 在python中运行的结果是：
# 总结：
