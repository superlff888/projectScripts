# -*- coding=utf-8 -*-
# @Time    : 2023/01/20 10:52
# @Author  : ╰☆H.俠ゞ
# =============================================================


class Stu:

    def __init__(self, id, name, phone, qq, score, sex=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.qq = qq
        self.score = score
        self.sex = sex

    def __str__(self):
        return f'{self.id}, {self.name}, {self.phone}, {self.qq}, {self.score}'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_qq(self):
        return self.qq

    def set_qq(self, qq):
        self.qq = qq

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


if __name__ == '__main__':
    print(Stu('1', 'lee', '15715151020', '1310157572', '90'))