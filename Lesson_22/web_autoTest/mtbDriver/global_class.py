# -*- coding=utf-8 -*-
# @Time    : 2022/09/18 21:48
# @Author  : ╰☆H.俠ゞ
# =============================================================
class Global_demo:
    def a(self):
        globals()["tmp"] = "100"  # 将下个函数要使用的值声明为全局变量
        # return globals()["tmp"]  # 返回全局变量
        print('你的值是什么', globals().keys())
        print('你的值是什么', globals().values())
        print(f'\n============================================================\n{globals()["tmp"]}')
        assert globals()["tmp"] == "100"

    def b(self):
        b = globals().get('tmp')
        print(b)


if __name__ == "__main__":
    Global_demo().a()
    Global_demo().b()
