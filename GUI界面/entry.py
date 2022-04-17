# -*- coding:utf-8 -*-
# 时间：2021年3月24日22:22:46
# 功能：生成文本框
# 目的：
import tkinter as tk


def fun():
    return 12


root = tk.Tk()
text = tk.Entry(width=20)
text.bind(sequence='<Button-1>')
text.pack()
root.mainloop()

# 在python中运行的结果是：
# 总结：
