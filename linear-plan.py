import numpy as np  # 矩阵处理
from scipy import optimize  # 线性求解

# 全局变量
debug = False
month = 6
product_type = 7
tool_type = 5

# 写出目标函数
x_target = [10.0, 6.0, 3.0, 4.0, 11.0, 9, 3]
y_target = [-0.5] * product_type
month_x = (x_target + y_target) * month
month_x[-7:] = list(map(lambda x: x - sum(x_target), month_x[-7:]))
c = np.array(month_x)
if not debug:
    print(c)  # 求最大值必须要取反

# 写出所有的不等式约束
x_1 = np.eye(product_type, product_type)
y_1 = -1 * np.eye(product_type, product_type)
a_1 = np.concatenate((x_1, y_1, np.zeros((product_type, product_type * (month - 1) * 2))), axis=1)  # 销量系数矩阵
m_1 = np.array([[0.5, 0.7, 0.0, 0.3, 0.2, 0.0, 0.5],
                [0.1, 0.2, 0, 0.3, 0, 0.6, 0],
                [0.2, 0, 0.8, 0, 0, 0, 0.6],
                [0.05, 0.03, 0, 0.07, 0.1, 0, 0.08],
                [0, 0, 0.01, 0, 0.05, 0, 0.05]])  # 时间矩阵

np.set_printoptions(threshold=np.inf, suppress=True)
a_matrix = np.array([])
for i in range(month):
    zero_r_matrix = np.zeros((5, product_type * ((5 - i) * 2 + 1)))
    zero_l_matrix = np.zeros((5, product_type * i * 2))
    material_proc = np.concatenate((zero_l_matrix, m_1, zero_r_matrix), axis=1)
    if i == 0:
        result = np.concatenate((a_1, material_proc), axis=0)
        a_matrix = result
        continue
    sale_proc = []
    for j in range(product_type):
        lst = [0] * month * product_type * 2
        lst[product_type * i * 2 + j] = 1
        lst[product_type * (i * 2 - 1) + j] = 1
        lst[product_type * (i * 2 + 1) + j] = -1
        sale_proc.append(lst)
    result = np.concatenate((sale_proc, material_proc), axis=0)
    a_matrix = np.concatenate((a_matrix, result), axis=0)

if not debug:
    print(len(a_matrix), len(a_matrix[0]))

# 右侧向量
sale_matrix = [[500, 1000, 300, 300, 800, 200, 100],
               [600, 500, 200, 0, 400, 300, 150],
               [300, 600, 0, 0, 500, 400, 100],
               [200, 300, 400, 500, 200, 0, 100],
               [0, 100, 500, 100, 1000, 300, 0],
               [500, 500, 100, 300, 1100, 500, 60]
               ]  # 先写销售量约束
materials = [[4 - 1, 2, 3, 1, 1],
             [4, 2 - 2, 3, 1, 1],
             [4, 2, 3, 1 - 1, 1],
             [4, 2 - 1, 3, 1, 1],
             [4 - 1, 2 - 1, 3, 1, 1],
             [4, 2, 3 - 1, 1, 1 - 1]]  # 材料约束
b_matrix = []
for i in range(len(sale_matrix)):
    b_matrix += sale_matrix[i] + \
                [material * 2 * 8 * 24 for material in materials[i]]
print(len(b_matrix))
if debug:
    for i in range(len(b_matrix)):
        if i % 12 == 0:
            print('\n')
        print(b_matrix[i], end='\t')

# 写出等式约束
equal_len = month * product_type * 2

a_eq = [[0] * equal_len for _ in range(product_type)]  # 创建一个7行84列的全0嵌套列表
for i in range(product_type):
    a_eq[i][-7 + i] = 1

b_eq = [50] * product_type
if debug:
    for i in range(len(a_eq)):
        print(f'第{i}个序列长度：', len(a_eq[i]))
        print(a_eq[i][-7:])

# 写出变量取值范围的约束
x_bounds = [(0, None)] * product_type
y_bounds = [(0, 100)] * product_type
bounds = (x_bounds + y_bounds) * month
if debug:
    for i in range(len(bounds)):
        if i % 7 == 0:
            print('\n')
            print(bounds[i], end='\t')

res = optimize.linprog(-c,
                       A_ub=a_matrix, b_ub=b_matrix,
                       A_eq=a_eq, b_eq=b_eq,
                       bounds=bounds, method='highs', integrality=1)

if not res.success:
    print('执行失败')
print("最大利润为", -res.fun)

tmp_month = 0
ref = -1
for i in res.x:
    if ref != (tmp_month // product_type):
        if tmp_month // product_type % 2 == 0:
            print(f'\n第{tmp_month // 14 + 1}月')
        else:
            print()
        ref = tmp_month // product_type
    if tmp_month // product_type % 2 == 0:
        print(f'生产量x{tmp_month % product_type}:{i}', end='\t')
    else:
        print(f'库存量x{tmp_month % product_type}:{i}', end='\t')
    tmp_month += 1
