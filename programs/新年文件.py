# 时间：2021年2月11日22:13:59
# 功能：
# 目的：
print('牛年快乐')

for niu in range(1000):
    if niu == niu/6+niu/12+niu/7+5+niu/2+4:
        print(niu)
    else:
        pass

# 对丢番图问题的求解
nian = 1
while nian != nian/6+nian/12+nian/7+5+nian/2+4:
    nian += 1
else:
    print(nian)

# 百鸡百钱问题
for w in range(20):
    for q in range(33):
        if 7*w+4*q == 100:
            print(q, w, 100-q-w)

print('-----------------------')
for x in range(0, 20):
    if (300+3*x) % 4 == 0 and 100-x-(300+3*x)/4 >= 0 and (300+3*x)/4 >= 0:
        print(x, int(100-x-(300+3*x)/4), int((300+3*x)/4))


# 数学黑洞问题
"""狐狸为啥不吃草"""
from itertools import combinations

def menu_data(nums):
    # 用字符串的下标操作取出各个位数
    a = nums[0]  # 千
    b = nums[1]  # 百
    c = nums[2]  # 十
    d = nums[3]  # 个
    if not a == b == c == d:
        list1 = [a, b, c, d]  # 去除list1中各个位数都相同的数
        for i in combinations(list1, 4):
            i = list(i)
            print(i, end='')
        sums = 0
        while True:
            small = int(''.join(sorted(i)))
            # print(f'第{sums+1}次,较小数{small}')
            big = int(''.join(sorted(i, reverse=True)))
            # print(f'第{sums+1}次,较大数{big}')
            difference = big - small
            # print(f'第{sums+1}次,两数差{difference}')
            sums += 1
            if difference == 6174:
                print(f'结果为:6174,一共用了:{sums}')
                break
            else:
                i = list(str(difference))
                # print(i)
                if len(i) < 4:
                    i.append('0')
                # print(i)


def main():
    for i in range(1000, 10000):
        nums = str(i)
        menu_data(nums)


main()


# 在python中运行的结果是：
# 总结：
