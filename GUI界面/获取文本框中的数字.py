# -*- coding:utf-8 -*-
# 时间：2021年3月21日17:04:10
# 功能：
# 目的：
# -*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()  # 建立窗口window
window.title('示例1')  # 窗口名称
window.geometry("400x240")  # 窗口大小(长＊宽)

textExample = tk.Text(window, height=10)  # 文本输入框
textExample.pack()  # 把Text放在window上面，显示Text这个控件


def getTextInput():
    result = textExample.get("1.0", "end")  # 获取文本框输入的内容
    tim = tk.Label(window, text='{0}'.format(result), font=('Arial', 12), width=30, height=2)
    tim.pack()


# Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
# "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。

# 按钮（#command绑定获取文本框内容的方法）
btnRead = tk.Button(window, height=1, width=10, text="Read", command=getTextInput)
btnRead.pack()  # 显示按钮

window.mainloop()  # 显示窗口

# 在python中运行的结果是：
# 总结：
