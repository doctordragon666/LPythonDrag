# -*- coding:utf-8 -*-
# 日期：2021年11月14日21点35分
# 功能：查找重复文件
# 目的：
import os
lst = []
for path, lst, file_lst in os.walk("F:/作业/WORD（个人类和作业过期类）"):
    with os.scandir(path=path) as it:
        for file_name in it:
            if file_name.is_file():
                file = open(file_name, "rb").read()
                if hash(file) in lst:
                    os.remove(file_name)
                else:
                    lst.append(hash(file))

# 在python中运行的结果是：
# 总结：
