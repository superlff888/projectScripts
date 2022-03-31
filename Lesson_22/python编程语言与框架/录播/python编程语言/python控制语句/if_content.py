# -*- coding=utf-8 -*-
# @Time    : 2022/03/31 20:06
# @Author  : ╰☆H.俠ゞ
# =============================================================

class AddOn:
    def addon(self):
        self.add = None

    def if_my(self):
        content = "scdlfvbn"
        if content:  # 相当于content == "scdlfvbn"的执行结果是True
            return content
        else:
            print("false")


a = AddOn()
a.if_my()
