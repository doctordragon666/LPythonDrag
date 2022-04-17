# -*- coding:utf-8 -*-
# 时间：2021年3月21日16:12:16
# 功能：
# 目的：
import tkinter as tk

# 第1步，实例化object，建立窗口window，并设定基本参数
window = tk.Tk()
window.title('来玩玩吧')
window.geometry('500x100')

# 第2步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
L = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高
L.pack()

# 为按钮功能建立一个函数，该函数必须创建在之前。
click = False


def buttons():
    global click
    if not click:
        click = True
        var.set('张位辉戴上了绿帽,并表示爱不释手~')
    else:
        click = False
        var.set('')


# 第3步，在窗口界面设置放置Button按键
b = tk.Button(window, text='戴帽子（点我）', font=('Arial', 12), width=20, height=1, command=buttons)
b.pack()

# 收尾，激活
window.mainloop()


# 在python中运行的结果是：
# 总结：
