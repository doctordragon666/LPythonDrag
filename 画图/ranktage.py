# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#
import os
import turtle

def eql_mul_side(f_len_num, f_side_num):
    """画一个矩形"""
    pen = turtle.Pen()  # 创建一个笔对象
    pen.pencolor('blue')  # 上颜色
    for i in range(f_side_num):
        pen.forward(f_len_num)  # 向前x个单位
        pen.left(360 / f_side_num)  # 转向


def tree(f_len, f_pen):
    """画树"""
    if f_len > 5:
        f_pen.forward(f_len)
        f_pen.right(20)
        tree(f_len - 10, f_pen)
        f_pen.left(40)
        tree(f_len - 10, f_pen)
        f_pen.right(20)
        f_pen.backward(f_len)


if __name__ == '__main__':
    # len_num = int(input('请输入边长'))
    # side_num = int(input('请输入边数'))
    # eql_mul_side(len_num, side_num)
    # print(f'正{side_num}边形生成完毕，长度为{len_num}')
    t = turtle.Turtle()  # 创建一个海龟对象
    myWin = turtle.Screen()  # 创建一个画布
    t.left(90)
    t.up()  # 抬起画笔
    t.backward(100)
    t.down()  # 放下画笔
    t.color("green")
    tree(30, t)
    myWin.exitonclick()  # 点击退出

    os.system('pause')
# 运行结果
