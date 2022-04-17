# -*- coding:utf-8 -*-
# 时间：2021年3月21日16:18:18
# 功能：
# 目的：
# 第1步
import tkinter as tk
window = tk.Tk()
window.title('性别测试')
window.geometry('500x150')

# 第2步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
L = tk.Label(window, bg='yellow', width=20, text='你的性别？')
L.pack()


# 第3步，定义选项触发函数功能
def sex_selection():
    L.config(text='你....' + var.get())


# 第4步，创建三个独立选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，
# 把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text='男', variable=var, value='是帅哥啊', command=sex_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='女', variable=var, value='是靓妹呀', command=sex_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='？', variable=var, value='你不是人？？？', command=sex_selection)
r3.pack()

window.mainloop()

# 在python中运行的结果是：
# 总结：
