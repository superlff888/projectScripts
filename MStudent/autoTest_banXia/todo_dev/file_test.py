# -*- coding=utf-8 -*-
# @Time    : 2023/01/23 20:25
# @Author  : ╰☆H.俠ゞ
# =============================================================
from MStudent.autoTest_banXia.todo_dev.students import Stu


class FileOp:

    def __init__(self):
        self.file = r'/autoTest_banXia/todo_dev\data.txt'

    # 读取
    def read(self):  # 根据业务要求，处理成字典格式的中间数据  stu_dict = {id: stu}
        stu_dict = {}
        with open(self.file, mode='r', encoding='utf-8') as f:
            # print(f.readlines())
            for readline in f.readlines():
                line_split = readline.split(",")
                id = line_split[0]
                name = line_split[1]
                phone = line_split[2]
                qq = line_split[3]
                score = line_split[4].strip()  # 默认删除当前字符串的首尾的空格和换行符
                stu = Stu(id, name, phone, qq, score)
                stu_dict[id] = stu
        return stu_dict

    # 写入
    def write(self, stu_dict: dict):
        with open(self.file, mode='w', encoding='utf-8') as f:  # mode = 'w' ,覆盖写入
            for stu in stu_dict.values():
                f.write(str(stu))  # 强制转化为字符串，将Stu类实例转化为str类实例
                f.write('\n')


if __name__ == '__main__':
    print(FileOp().read())