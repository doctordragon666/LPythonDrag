# -*- coding:utf-8 -*-
# 时间：2021年3月21日16:26:18
# 功能：
# 目的：
# -*- coding=utf-8 -*-

import tkinter as tk

root_window = tk.Tk()
root_window.title('Tkinter_Demo')
root_window.geometry('400x300')

hello_label = tk.Label(root_window, text='hello world', bg='red', width=10, height=2)
hello_label.pack(side=tk.TOP)  # 这里的side可以赋值为LEFT  RIGHT TOP  BOTTOM

root_window.mainloop()

'''
anchor 文本的位置
background(bg) 背景色
border_width(bd) 边框宽度
bitmap 位图
font 文本的字体
fore_ground(fg) 前景色
height 高度
image 图片
justify 多行文本的对齐方式
text 指定标签中的文本
width 指定标签的宽度
'''
# 在python中运行的结果是：
# 总结：
