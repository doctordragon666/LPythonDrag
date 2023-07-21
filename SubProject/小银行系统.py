# 时间：2021年1月29日14:35:32
# 功能：模拟银行的低级系统
# 目的：测试if的功能
class Bank:
    def __init__(self, key_list):
        self.key_list = key_list
        try:
            self.money = int(open('老板的账户余额.txt', 'r').read())
        except FileNotFoundError:
            self.money = 0

    @staticmethod
    def welcome():
        print('欢迎您使用银行系统')
        a = int(input('请输入用户名'))
        return a

    def save_money(self):
        num = int(input('请输入您的存款金额'))
        self.money += num

    def take_money(self):
        c = int(input('您想取多少钱'))
        if c > self.money:
            print('余额不足')
        else:
            self.money -= c

    def save(self):
        print('您的余额为', self.money)
        with open('老板的账户余额.txt', 'w') as p:
            print(self.money, file=p)


def order(self_bank):
    x = int(input('请输入密码'))
    if x == 123456:
        while True:
            b = input('你是存钱还是取钱')
            if b == '存钱':
                self_bank.save_money()
            else:
                self_bank.take_money()
            c = input('你想继续吗？ 输入yes/no')
            if c == 'yes':
                continue
            else:
                self_bank.save()
                return 0
    else:
        print('密码错误，请重新输入')
        return True


def main():
    lst = (120, 119, 110, 911)
    self_bank = Bank(lst)
    a = self_bank.welcome()
    while True:
        if a in lst:
            for item in range(3):
                if order(self_bank):
                    continue
                else:
                    exit()
        else:
            print("银行卡不存在")
            break


if __name__ == '__main__':
    main()


# 在python中运行的结果是：
# 总结：
