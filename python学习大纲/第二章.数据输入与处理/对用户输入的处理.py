# 时间：2020年2月19日11:13:19
# 作者：river stream
# 功能：
# 目的：
import traceback  # traceback 导入后可打印异常信息

"""
常见的错误类型
变量未定义
缩进过多
冒号缺失
syntax error 语法错误
index error 索引（导入模块出错）错误
value error 值错误
attribute error 调用不存在的方法
EFO error 遇到文件末尾引发异常
IOE error input /output操作引发的异常，打开文件出错
key error 字典中不存在该关键字
name error 使用不存在的变量名字
Tab error 缩进错误
zero division error 除数为0 
"""

# 对用户的错误输入的处理
try:
    a = int(input('输入你的年龄'))
    assert a != 21231  # 一旦输入的数据不满足assert后的条件表达式就会抛出异常
    b = 100 / a            # 将用户的输入代码放在try下，判断用户的输入数据
except ZeroDivisionError:
    print('年龄不能为0')  # 用EXCEPT来输出不同的异常操作的提示，可以不写任何错误类型
except ValueError:
    print('请输入数字')
    # traceback.print_exc()  # 打印异常信息
else:
    if a > 100:
        print('错误')
    else:
        print('你的年龄为', 100/b)
# 如果没错误才会执行else，否则会结束程序
# 此外还可使用finally,无论有无异常都会输出和运行
finally:
    print('--------------------')
#
# try:
#     r = int(input('请输入圆的半径'))
#     if r == 0:
#         raise Exception('半径不能为0')  # 手工抛出异常
# except Exception as e:  # 将异常转化为提示信息，并转化为一种错误类型
#     print(e)
# 在python中运行的结果是：
# 输入你的年龄190
# 错误
# --------------------
# 请输入圆的半径0
# 半径不能为0
# 总结：
