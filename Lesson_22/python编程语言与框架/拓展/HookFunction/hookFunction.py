# @Time  : 2022/01/04 23:59
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import time


class LazyPerson:
    def __init__(self, name):
        self.name = name  # 构造函数定义类属性，类方法直接引用该属性值
        self.watch_tv_func = None
        self.have_dinner_func = None

    def get_up(self):
        print("%s get up at:%s" % (self.name, time.time()))

    def go_to_sleep(self):
        print("%s go to sleep at:%s" % (self.name, time.time()))

    def register_tv_hook(self, watch_tv_func):
        self.watch_tv_func = watch_tv_func

    def register_dinner_hook(self, have_dinner_func):
        self.have_dinner_func = have_dinner_func

    def enjoy_a_lazy_day(self):

        # get up
        self.get_up()
        time.sleep(3)
        # watch tv
        # check the watch_tv_func(hooked or unhooked)
        # hooked
        if self.watch_tv_func is not None:
            self.watch_tv_func(self.name)
        # unhooked
        else:
            print("no tv to watch")
        time.sleep(3)
        # have dinner
        # check the have_dinner_func(hooked or unhooked)
        # hooked
        if self.have_dinner_func is not None:
            self.have_dinner_func(self.name)
        # unhooked
        else:
            print("nothing to eat at dinner")
        time.sleep(3)
        self.go_to_sleep()


def watch_daydayup(name):
    print("%s : The program ---day day up--- is funny!!!" % name)


def watch_happyfamily(name):
    print("%s : The program ---happy family--- is boring!!!" % name)


def eat_meat(name):
    print("%s : The meat is nice!!!" % name)


def eat_hamburger(name):
    print("%s : The hamburger is not so bad!!!" % name)


if __name__ == "__main__":
    lazy_tom = LazyPerson("Tom")
    lazy_jerry = LazyPerson("Jerry")
    # register hook
    lazy_tom.register_tv_hook(watch_daydayup)
    lazy_tom.register_dinner_hook(eat_meat)
    lazy_jerry.register_tv_hook(watch_happyfamily)
    lazy_jerry.register_dinner_hook(eat_hamburger)
    # enjoy a day
    lazy_tom.enjoy_a_lazy_day()
    lazy_jerry.enjoy_a_lazy_day()

"""
1、类中提供了两个钩子函数register_tv_hook、register_dinner_hook，钩子函数若实现了，就执行该函数
2、理解起来很简单：在特定的点执行的一个函数罢了；要提供通用的框架能力，框架自身去实现该方法功能，是没有意义的，
    所以框架给提供一个挂载的point，把具体逻辑的实现交给用户就好了，灵活可用。
"""
