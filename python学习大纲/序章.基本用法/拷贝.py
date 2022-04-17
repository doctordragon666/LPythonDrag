# 时间：2021年2月21日19:41:49
# 功能：
# 目的：浅拷贝和深拷贝，防止重复释放内存
# 浅拷贝，要导入cope模块
import copy
import abc


class Disk:
    @abc.abstractmethod
    def store(self):
        pass  # 抽象类


class Cpu:
    pass


class Computer(object):
    def __init__(self, m_cpu, m_disk):
        self.cpu = m_cpu
        self.disk = m_disk

    def __del__(self):
        del self.cpu
        del self.disk


cpu = Cpu()
disk = Disk()
computer = Computer(cpu, disk)
computer2 = copy.copy(computer)  # copy浅拷贝，deep cope 深度拷贝，完全不同的新数据
computer3 = copy.deepcopy(computer)
print(id(computer2), id(computer), id(computer3))
print(computer, computer3, computer2)
# 在python中运行的结果是：
# 总结：
