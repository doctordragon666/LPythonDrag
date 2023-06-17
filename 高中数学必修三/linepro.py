# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#
import numpy as np
from scipy import optimize

# 定义线性规划问题中的系数矩阵和常数向量
c = np.array([1, -2, 1, 0])
a = np.array([[2, -1, 4, 0],
              [-1, 2, -4, 0]])
b = np.array([8, 4])

# 定义等式约束的系数矩阵和常数向量
aeq = np.array([[1, 1, -2, 1]])
beq = np.array([10])

# 定义变量的上下界
x_bounds = [(0, None), (0, None), (0, None), (0, None)]

# 调用线性规划函数求解问题
res = optimize.linprog(c,
                       A_ub=a, b_ub=b,
                       A_eq=aeq, b_eq=beq,
                       bounds=x_bounds, method='highs')

print(res)

# 运行结果
