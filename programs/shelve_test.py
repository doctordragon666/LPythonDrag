# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#
import shelve

"""只会以键值对存储数据，并且存储数据的格式是键加元组"""
d = shelve.open('my_test')  # shelve的open只是打开文件名字，不能加后缀
d['name'] = 12
d['test'] = 11
del d['name']

flag = 'name' in d
k_lst = list(d.keys())

d['lst'] = [1,2,3,4]  # 不会保存为列表格式，底层会转化为元组

"""是元组，所以导出格式然后再修改"""
temp = d['lst']
temp.append(10)
d['lst'] = temp

print(d['lst'])

d.close()
# 运行结果
