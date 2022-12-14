# 时间：2021年2月20日19:28:51
# 功能：
# 目的：
# 1.求多个数之和
# def sum2(*a):
#     sum1 = 0
#     for i in a:
#         sum1 += i
#     return sum1
#
#
# print(sum2(12,232))
#
#
# # 2.找出列表中的奇数位的数。组成一个新列表并返回
# def sum3(*a):
#     lst = []
#     for i in a:
#         if i%2:
#             lst.append(i)
#     return lst

listtest = ["1", "2", "9", "0", "-1", "-2"]
# 自动排序
print("Sorted numerically:",
      sorted(listtest, key=lambda x: int(x)))

# filter过滤数组
print("Filtered positive even numbers:",
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), listtest)))

# 对列表批量操作用Map
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), listtest)))

# 在python中运行的结果是：
# 总结：
