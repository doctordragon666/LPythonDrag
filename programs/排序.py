# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#
lst = [3, 4, 2, 1, 5, 9, 0, 6, 8, 7]
max_item = 0
for i in range(len(lst)):
    for j in range(i, len(lst)):
        if lst[j] > lst[max_item]:
            lst[j], lst[max_item] = lst[max_item], lst[j]
    max_item = i


print(lst)
# 运行结果
