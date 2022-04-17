# 时间：2021年2月4日12:44:59
# 功能：
# 目的：
for index, item in enumerate(range(12)):
    print(index, item)
 # enumerate 枚举列表中的元素，并将其中顺序也拿出来

# continue的使用
# 求出某数的平方根，近似求法,向下取整
a = 0
x = int(input('请输入求平方根的数'))
while a**2 < x:
    if (a+1)**2 <= x:
        a += 2
        continue
    break
print(a)

# 使用for循环可以限定循环次数
# v = 1
# for i in range(3):
#     if v < 10:
#         v += 1
#         print(123)

# 在python中运行的结果是：

# 总结：
