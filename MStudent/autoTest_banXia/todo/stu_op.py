# -*- coding=utf-8 -*-
# @Time    : 2023/01/23 21:09
# @Author  : ╰☆H.俠ゞ
# =============================================================
from MStudent.autoTest_banXia.todo.file_test import FileOp


class StuOp:
    stu_dict = FileOp().read()

    # 查询
    @classmethod
    def queStu(cls, id):
        if id in cls.stu_dict:
            return cls.stu_dict[id]
        else:
            return '查询失败'

    @classmethod
    def add_stu(cls, stu):
        if stu.id in cls.stu_dict:
            return '不可重复新增'
        else:
            cls.stu_dict[stu.id] = stu
            FileOp().write(cls.stu_dict)
            # print(cls.stu_dict)
            return '新增成功'

    @classmethod
    def del_stu(cls, id):
        if id in cls.stu_dict:
            del cls.stu_dict[id]
            FileOp().write(cls.stu_dict)
            return '删除成功'
        else:
            return '删除失败'

    @classmethod
    def update_stu(cls, id, **kwargs):
        print(kwargs)
        if id in cls.stu_dict:
            stu = cls.stu_dict[id]
            if 'name' in kwargs:  # name为kwargs的key
                VALUE = kwargs['name']
                stu.set_name(VALUE)
            if 'phone' in kwargs:
                phone = kwargs['phone']
                stu.set_phone(phone)
            if 'qq' in kwargs:
                qq = kwargs['qq']
                stu.set_qq(qq)
            if 'score' in kwargs:
                score = kwargs['score']
                stu.set_score(score)
            FileOp().write(cls.stu_dict)
            return '修改成功'
        else:
            return '修改失败'


if __name__ == '__main__':
    print(StuOp.queStu('1'))
    # print(StuOp.add_stu(Stu('8', 'lff', '15715151010', '1310157578', '100')))
    # print(StuOp.del_stu('77'))
    print(StuOp.update_stu('1', name='lisa', score='88'))