# -*- coding:utf-8 -*-
# 时间：2021年3月21日16:33:25
# 功能：
# 目的：
# -*- coding=utf-8 -*-

import tkinter

root_window = tkinter.Tk()
root_window.title('Tkinter_Demo')
root_window.geometry('400x300')

# main frame
main_frame = tkinter.Frame(root_window)
main_label = tkinter.Label(main_frame, text='主框架')
main_label.pack()

# left frame
left_frame = tkinter.Frame(main_frame)
left_label = tkinter.Label(left_frame, text='左框架')
left_label.pack()
left_frame.pack(side=tkinter.LEFT)

# right frame
right_frame = tkinter.Frame(main_frame)
right_label = tkinter.Label(right_frame, text='右框架')
right_label.pack()
right_frame.pack(side=tkinter.RIGHT)

main_frame.pack()

root_window.mainloop()


# 在python中运行的结果是：
# 总结：
