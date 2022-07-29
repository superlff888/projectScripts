# -*- coding=utf-8 -*-
# @Time    : 2022/07/29 23:50
# @Author  : ╰☆H.俠ゞ
# =============================================================
class X(object):
    def __init__(self, a, b, range):
        self.a = a
        self.b = b
        self.range = range

    def __call__(self, a, b):
        self.a = a
        self.b = b
        print('__call__ with （{}, {}）'.format(self.a, self.b))

    def __del__(self):
        del self.a
        del self.b
        del self.range
        # print(self.a, self.b, self.range)

    def del_data(self):
        print(self.a, self.b, self.range)


x = X(1, 2, 3)
x(2, 3)  # 实例对象加括号就可以如函数一样调用
x.del_data()  # python内存清理机制，最后才执行魔法函数__del__
