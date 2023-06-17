# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#
import numpy as np
from scipy import optimize

c = np.array([10, 24, 7])
a_matrix = np.array([[-2, -3, 0],
                     [-1, -3, -1]])
b_matrix = np.array([-6, -4])
u_bound = [(0, None)] * 3

res = optimize.linprog(c, A_ub=a_matrix, b_ub=b_matrix,
                       bounds=u_bound)
print(res)
# 运行结果
