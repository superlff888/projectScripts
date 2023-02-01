# -*- coding=utf-8 -*-
# @Time    : 2023/01/24 09:49
# @Author  : ╰☆H.俠ゞ
# =============================================================
from MStudent.autoTest_banXia.todo_dev.stu_op import StuOp
from MStudent.autoTest_banXia.todo_dev.students import Stu


def run():
    op = int(input('请输入你的操作：'))
    if op == 3:
        id = input('请输入id:')
        kwargs = input('请输入修改信息：')
        kwargs = eval(kwargs)
        print(StuOp.update_stu(id, **kwargs))
    if op == 1:
        ID = input('请输入id:')
        print(StuOp.del_stu(ID))
    if op == 2:
        id = input('请输入id：')
        name = input('请输入name：')
        phone = input('请输入phone：')
        qq = input('请输入qq：')
        score = input('请输入score：')
        stu = Stu(id, name, phone, qq, score)
        StuOp.add_stu(stu)


run()
