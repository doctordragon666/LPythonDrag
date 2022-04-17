# 作业1 猜年龄
while True:
    print('游戏开始')
    answer = input('你想（开始）继续吗,请输入 Y/y 或者 N/n ')
    if answer == 'Y' and 'y':
        age1 = int(input('你觉得我的年龄有多大'))
        for i in range(3):
            if age1 == 12:
                exit()
            elif age1 > 12:
                print('猜大了')
            elif age1 < 12:
                print('猜小了')
            else:
                continue
    else:
        break

# 作业2 计算BIM
height, weight = 1.75, 80.5
BIM = weight / height**2
if BIM < 18.5:
    print('过轻')
elif BIM < 25:
    print('正常')
elif BIM < 28:
    print('过重')
elif BIM < 32:
    print('肥胖')
else:
    print('过度肥胖')
