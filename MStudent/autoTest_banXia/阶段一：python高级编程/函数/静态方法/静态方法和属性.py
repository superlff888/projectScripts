# -*- coding=utf-8 -*-
# @Time    : 2022/10/23 16:06
# @Author  : ╰☆H.俠ゞ
# =============================================================
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


if __name__ == "__main__":
    s = Student()
    s.birth = 18
    print(s.birth)
