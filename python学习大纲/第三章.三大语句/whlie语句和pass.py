# 时间：2021年2月3日09:32:45
# 功能：
# 目的：复习所学知识

# while语句的使用
lst = [1, 2, 3, 4, 5]
j = lst[1:4]
while j not in lst:
    print(lst)
    break  # break用于终止while（无break且为假时则执行else）
else:
    print(j)

# while的嵌套循环
# while []:
#     while {}:
#         print('shutdown')
#     else:
#         print('victory')
# else:
#     while i != 5:
#         print('立春快乐')
#         break

# 在讲for in 之前，先了解range函数
r = range(23)
z = range(1, 23)
p = range(1, 56, 5)
print(list(r), list(z), list(p))
# range(start, stop, step)函数
# 不能直接输出这里的r,z,p否则只会输出数列名字。要用list（变量名字），list(range(...))才能打印出

# while常与if语句混用，下面对if语句进行更深理解
a = 23
if a % 2 == 0:
    print('error')
else:
    print('right')
''' 该式等价于上式'''
if not bool(a % 2):
    print('error')
else:
    print('right')

# 总结：
