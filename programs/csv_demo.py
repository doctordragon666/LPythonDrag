# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#

import csv

read = csv.reader()
dic = {'name':12}
write = csv.writer()
write.writerow(dic) # 写入字典
readd = csv.DictReader()

writee = csv.DictWriter()
writee.writeheader()
# 运行结果
