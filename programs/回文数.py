# 时间：2021年2月6日16:44:34
# 功能：求回文数（原版已经删除）
# 目的：了解算法的重要性


def f(p, val):
    m = p
    s = 0
    while m:
        s = s * 10 + m % 10
        m //= 10

    if s == p:
        print(f'{p}是回文数')
    elif val == '2':
        pass
    else:
        print('该数字不是回文数')


if __name__ == '__main__':
    print('请选择如下功能')
    print('1.验证单个数字是否为回文数，2.求出特定范围内的回文数')
    answer = input('请输入数字')
    if answer == '1':
        i = int(input('请输入该数字'))
        f(i, answer)
    else:
        i = int(input('请输入范围(数字只能为整数，且暂支持输入上限)'))
        t = 0
        for x in range(i):
            f(x, answer)


# 在python中运行的结果是：
# 总结：
