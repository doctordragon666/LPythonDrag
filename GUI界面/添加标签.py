# -*- coding:utf-8 -*-
# 时间：2021年3月11日22:03:11
# 功能：
# 目的：

import tkinter as tk
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('Tkinter:从入门到放弃')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('600x200')  # 这里的乘是小x
# 第4步，在图形界面上设定文本标签(为了阅读性分开构建)
l = tk.Label(window, text='论如何卸载python？', font=('Arial', 12), width=30, height=2, bg='green')
# 说明： bg为背景，text为文本内容，font为字体，width为长，height为高，这里的长和高是字符的长和高。
# 第5步，放置标签
l.pack()
# 收尾:激活GUI窗口
window.mainloop()


# 在python中运行的结果是：
# 总结：
