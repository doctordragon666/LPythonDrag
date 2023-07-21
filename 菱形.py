# 时间：2021年2月4日17:04:30
# 功能：打印菱形
# 目的：灵活处理字符串

# 上半部分菱形
for i in range(1, 13):
    spaces = " " * (12 - i)
    stars = "*" * (2 * i - 1)
    line = f"{spaces}{stars}"
    print(line.center(50))

# 下半部分菱形
for i in range(11, 0, -1):
    spaces = " " * (12 - i)
    stars = "*" * (2 * i - 1)
    line = f"{spaces}{stars}"
    print(line.center(50))


# 在python中运行的结果是：
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# 总结：
