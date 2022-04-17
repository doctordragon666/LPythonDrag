# 多分支结构
# 时间：2021年1月29日14:03:49
# 功能：测试if的价格
# 目的：自动判断成绩系统
score = int(input('您的成绩是'))
if score > 100:
    print('夜郎自大无耻至极')
elif score > 90:
    print('能安之者其在君乎')
elif score > 60:
    print('过犹不及中庸之道')
elif score > 0:
    print('业精于勤荒于嬉')
else:
    print('君不鸣则已，一鸣惊人，何必如此自卑')

# 此外也可使用条件表达式简化代码：x if (a) else y
# 逻辑为如果a 为Ture则输出x，如果为False则输出y。必须要输出，否则报错
# 用条件表达式比较两个数字的大小
num1, num2 = int(input('请输入第一个数字')), int(input('请您输入第二个数字'))
print(str(num1)+'大于等于'+str(num2) if (num1 >= num2) else str(num1)+'小于'+str(num2))

# if的嵌套结构
score_dic = {'张三': 99, '李四': 59}
reply = input('请输入您的姓名')
if reply in score_dic.keys():
    if score_dic[reply] > 60:
        print('你及格了')
    else:
        print('你没及格')
else:
    print('你落榜了')
# 在python中运行的结果是：
# 总结：
