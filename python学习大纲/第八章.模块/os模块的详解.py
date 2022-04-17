# 时间：2021年2月22日16:07:53
# 功能：
# 目的：

import os
# os模块详解
print(os.times())  # 找到系统时间
os.system('ipconfig')  # 相当于使用cmd命令
os.startfile("F:\\MCLauncher\\Resource\\剑起千波的世界\\world_icon.jpeg")  # 直接调用可执行程序
print(os.listdir())  # 为空时返回当前的文件信息，否则返回括号内的
os.mkdir('F:\\python\\pythonProject1\\venv\\python学习大纲\\第八章虚无')  # 创建新目录
os.makedirs('new/new1/new2/new3')  # 创建多级目录
os.rmdir('F:\\python\\pythonProject1\\venv\\python学习大纲\\第八章虚无')  # 删除该目录
os.removedirs('new/new1/new2/new3')  # 删除多级目录
os.chdir('F:\\python\\pythonProject1\\venv\\python学习大纲\\第八章.模块')  # 将该目录设置为工作目录
print(os.getcwd())  # 返回当前的工作目录

# os.path模块详解
print(os.path.abspath('内置模块.py'))  # 返回该文件的绝对路径
print(os.path.exists('内置模块.py'))  # 判断该文件是否存在
print(os.path.join('F:\\python', '内置模块.py'))  # 将目录与目录文件名字连接起来
print(os.path.split('F:\\python\\pythonProject1\\venv\\python学习大纲\\第八章.模块\\os模块的详解.py'))  # 将文件名和前面的分离
print(os.path.splitext('内置模块.py'))  # 分离扩展名
print(os.path.basename('F:\\python\\pythonProject1\\venv\\python学习大纲\\第八章.模块'))  # 从目录中提取文件名字
print(os.path.dirname('F:\\python\\pythonProject1\\venv\\python学习大纲\\第八章.模块'))  # 提取文件路径
print(os.path.isdir('内置模块.py'))  # 判断是否为路径

# 获取指定目录下的文件
path = os.getcwd()
lst = os.listdir(path)
lst2 = os.walk(path)
for a, b, c in lst2:
    # print(a, b, c, '\n')
    for i in b:
        print(os.path.join(a, i))
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
# 在python中运行的结果是：
# 总结：
