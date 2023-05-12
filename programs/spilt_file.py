# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#

# filename = input('请输入文件名')
filename = r"D:\File\WeChat Files\wxid_hszwingzt2k022\FileStorage\File\2022-11\所有致谢.txt"
with open(filename, 'r', encoding='utf-8') as f:
    lst = f.readlines()

for i in range(len(lst)):
    if i % (len(lst)//4) == 0:
        print('----')
    else:
        print(lst[i], end='')

# 运行结果
