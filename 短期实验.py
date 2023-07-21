# -*- coding:utf-8 -*-
# 本代码仅用与短期的实验，作为测试功能使用，请不要在这里进行笔记和文件的操作


# 请不要迅速关闭界面，保存7天以上

nums = 0
for i in range(2, 1000):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        nums += 1
        print(i)
print(f'has {nums} primer')
