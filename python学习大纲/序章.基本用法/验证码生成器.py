# coding:utf-8
# 时间：2021年3月10日20:14:52
# 功能：生成验证码
# 目的：对解释器进行运算
import string
import random
message = ''
words = ''.join((string.ascii_letters, string.digits))  # 生成大小写字母和数字串
for i in range(11):
    message += random.choice(words)
print(message)
# 在python中运行的结果是：
# 总结：
