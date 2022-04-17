# -*- coding:utf-8 -*-
# 时间：2021年3月21日16:21:44
# 功能：
# 目的：
import tkinter as tk
# 第1步
window = tk.Tk()
window.title('我的老婆')
window.geometry('500x100')

# 第2步，在图形界面上创建一个标签label用以显示并放置
L = tk.Label(window, bg='yellow', width=20, text='小孩子才做选择')
L.pack()


# 第3步，定义触发函数功能
def wife_selection():
    if (var1.get() == 1) & (var2.get() == 0):  # 如果选中第一个选项，未选中第二个选项
        L.config(text='我喜欢周冬雨 ')
    elif (var1.get() == 0) & (var2.get() == 1):  # 如果选中第二个选项，未选中第一个选项
        L.config(text='我喜欢关晓彤')
    elif (var1.get() == 0) & (var2.get() == 0):  # 如果两个选项都未选中
        L.config(text='我两个都不喜欢')
    else:
        L.config(text='我全都要')  # 如果两个选项都选中


# 第4步，定义两个Checkbutton选项并放置
var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='周冬雨', variable=var1, onvalue=1, offvalue=0,
                    command=wife_selection)  # 传值原理类似于radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='关晓彤', variable=var2, onvalue=1, offvalue=0, command=wife_selection)
c2.pack()

# 收尾，激活
window.mainloop()

# 在python中运行的结果是：
# 总结：
