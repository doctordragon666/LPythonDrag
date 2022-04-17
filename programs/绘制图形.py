# -*- coding:utf-8 -*-
# 时间：2021年3月12日09:21:41
# 功能：绘制图形
# 目的：创建一个GUI界面
import tkinter


class MyButton:

    def __init__(self, root, canvas, label, type):
        self.root = root
        self.canvas = canvas
        self.label = label

        if type == 0:
            button = tkinter.Button(root, text='画线', command=self.DrawLine)
        elif type == 1:
            button = tkinter.Button(root, text='画半圆形', command=self.DrawArc)
        elif type == 2:
            button = tkinter.Button(root, text='矩形工具', command=self.DrawRec)
        else:
            button = tkinter.Button(root, text='半椭圆工具', command=self.DrawOval)
        button.pack(side='left')

    def DrawLine(self):
        self.label.text.set('画线')
        self.canvas.SetStatus(0)

    def DrawArc(self):
        self.label.text.set('三角形工具')
        self.canvas.SetStatus(1)

    def DrawRec(self):
        self.label.text.set('矩形工具')
        self.canvas.SetStatus(2)

    def DrawOval(self):
        self.label.text.set('椭圆工具')
        self.canvas.SetStatus(3)


class MyCanvas:
    def __init__(self, root):
        self.status = 0
        self.draw = 0
        self.root = root
        self.canvas = tkinter.Canvas(root, bg='white',
                                     width=600,
                                     height=480)
        self.canvas.pack()
        self.canvas.bind('<ButtonRelease-1>', self.Draw)
        self.canvas.bind('<Button-2>', self.Exit)
        self.canvas.bind('<Button-3>', self.Del)
        self.canvas.bind_all('<Delete>', self.Del)
        self.canvas.bind_all('<KeyPress-d>', self.Del)
        self.canvas.bind_all('<KeyPress-e>', self.Exit)

    def Draw(self, event):
        if self.draw == 0:
            self.x = event.x
            self.y = event.y
            self.draw = 1
        else:
            if self.status == 0:
                self.canvas.create_line(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 1:
                self.canvas.create_arc(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 2:
                self.canvas.create_rectangle(self.x, self.y, event.x, event.y)
                self.draw = 0
            else:
                self.canvas.create_oval(self.x, self.y, event.x, event.y)
                self.draw = 0

    def Del(self, event):
        items = self.canvas.find_all()
        for item in items:
            self.canvas.delete(item)

    def Exit(self, event):
        self.root.quit()

    def SetStatus(self, status):
        self.status = status


class MyLabel:
    def __init__(self, root):
        self.root = root
        self.canvas = canvas
        self.text = tkinter.StringVar()
        self.text.set('画线')
        self.label = tkinter.Label(root,
                                   textvariable=self.text,
                                   fg='red',
                                   width=50)
        self.label.pack(side='left')


if __name__ == '__main__':
    root = tkinter.Tk()
    canvas = MyCanvas(root)
    label = MyLabel(root)
    MyButton(root, canvas, label, 0)
    MyButton(root, canvas, label, 1)
    MyButton(root, canvas, label, 2)
    MyButton(root, canvas, label, 3)
    root.mainloop()
# 在python中运行的结果是：
# 总结：
