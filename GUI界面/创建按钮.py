# -*- coding:utf-8 -*-
# 时间：2021年3月21日15:58:27
# 功能：
# 目的：
import tkinter as tk
import tkinter.messagebox as tkMB  # 用以构建弹出窗口

window = tk.Tk()

# 为按钮功能建立一个函数，该函数必须创建在之前。


def buttons():
    tkMB.showinfo("好家伙", "你成功了")
    # 说明:前面为弹出窗口的标题,后面为弹出窗口的内容.


# 创建一个按钮,并（内容自己自由编写），供点击按钮时调用
b = tk.Button(window, text="点我", command=buttons)
# 说明:text为按钮中的文本内容，command通常为绑定的函数功能，
# 调用命令参数command=函数名，点击按钮后会执行该函数。
# 放置按钮
b.pack()

window.mainloop()


# 在python中运行的结果是：
# 总结：
