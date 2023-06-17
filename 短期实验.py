# -*- coding:utf-8 -*-
# 本代码仅用与短期的实验，作为测试功能使用，请不要在这里进行笔记和文件的操作
import tkinter as tk


def read():
    result = text1.get('1.0', 'end')
    print(result)
    return result


if __name__ == '__main__':
    root = tk.Tk()
    button = tk.Button(width=12, command=read, text='read')
    text1 = tk.Text(root, height=20)
    text2 = tk.Text(root, height=20)
    text2.pack()
    text1.pack()
    button.pack()
    root.mainloop()



# 请不要迅速关闭界面，保存7天以上
