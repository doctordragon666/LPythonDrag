# -*- coding:utf-8 -*-
# 时间：2021年3月11日21:42:58
# 功能：创建初始化GUI界面
# 目的：熟悉Tkinter的作用1
import tkinter as tk

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('Tkinter:从入门到放弃')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('600x200')  # 这里的乘是字母小x

# 收尾:激活GUI窗口
window.mainloop()

# 在python中运行的结果是：
# 总结：
