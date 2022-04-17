# -*- coding:utf-8 -*-
# 时间：2021年3月12日21:15:24
# 功能：
# 目的：
import tkinter
import tkinter.messagebox


def cmd():
    global n
    global button_text
    n += 1
    if n == 1:
        tkinter.messagebox.askokcancel('提示', 'error')
        button_text.set('name_error')
    elif n == 2:
        tkinter.messagebox.askquestion('已经结束')


n = 0
root = tkinter.Tk()
button_text = tkinter.StringVar()
button_text.set('good')
button = tkinter.Button(root, textvariable=button_text,
                        command=cmd)
button.pack()
root.mainloop()


# 在python中运行的结果是：
# 总结：
