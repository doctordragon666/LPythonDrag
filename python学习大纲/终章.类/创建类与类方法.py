# 时间：2021年2月19日11:59:20
# 功能：无
# 目的：复习


class Person:
    m_name = ''  # 直接定义在其内部的变量，成为类属性,属于静态属性
    __m_lover = 'jiang'  # 设置为私有变量
    m_old = 0

    def __init__(self, name, old):
        self.m_old = old
        self.m_name = name

    """构造函数"""
    @classmethod  # 类方法
    def cls_method(cls, name, old):
        cls.m_name = name + '1'
        cls.m_old = old + 1  # 没有初始化函数时也可以

    def birthday(self):
        print(f'恭喜你，{self.m_name} 迎来了自己的生日')

    def show(self):
        print(self.m_name, self.m_old, self.__m_lover)

    @staticmethod  # 静态方法
    def bless():  # 括号内不含有任何的符号，否则报错
        print('在你的生日到来之际，诚挚地献上我的三个祝愿：一愿你身体健康；二愿你幸福快乐；三愿你万事如意。')
        print('深深祝福你,永远拥有金黄的岁月,璀璨的未来!')
        print('你加了一岁,加了一份魅力,加了一份成熟,加了一份智慧')


def main():
    p1 = Person('yue', '18')
    print(p1.m_old, p1.m_name)
    p1.birthday()
    Person.bless()
    p1.his_old = 19
    p1.show()
    print(Person.m_old)

    # 动态绑定属性
    p1.nickname = 'bao'
    print(p1.nickname)


if __name__ == '__main__':
    main()

# 在python中运行的结果是：18 yue
# 恭喜你，yue 迎来了自己的生日
# 在你的生日到来之际，诚挚地献上我的三个祝愿：一愿你身体健康；二愿你幸福快乐；三愿你万事如意。
# 深深祝福你,永远拥有金黄的岁月,璀璨的未来!
# 你加了一岁,加了一份魅力,加了一份成熟,加了一份智慧
# yue 18 jiang
# 0
# bao
# 总结：
