# -*- coding=utf-8 -*-
# @Time    : 2022/10/16 09:27
# @Author  : ╰☆H.俠ゞ
# =============================================================


import random


"""
方式一
"""
random.randint(0, 300)  # 该下标就是员工在列表中的位置


"""
方式二
"""
prom = """
        按任意键开始抽奖
        """


def removeCd(emp_list):
    for emp in emp_list:
        empCd_list.remove(emp)  # 列表不支持批量删除，所以需要遍历删除


name = input(prom)

# 员工列表
empCd_list = [i for i in range(1, 301)]  # list(range(300))
# 先抽三等奖：从所有员工empCd_list中随机抽取30名
thirdPrizeEmps = random.sample(empCd_list, 30)
# 删除已获奖的员工，因为已获得三等type奖的30名员工不能继续参与抽奖
removeCd(thirdPrizeEmps)
# 获得三等奖的员工
print(f"获得三等奖的员工列表: {thirdPrizeEmps}")
# 从剩下的员工中抽取6名二等奖
secondPrizeEmps = random.sample(empCd_list, 6)
# 获得二等奖的员工
print(f"获得二等奖的员工列表: {secondPrizeEmps}")
# 删除已中二等奖的员工
removeCd(secondPrizeEmps)
# 从剩下的员工中抽取3名一等奖
firstPrizeEmps = random.sample(empCd_list, 3)
print(f"获得二等奖的员工列表: {firstPrizeEmps}")
removeCd(firstPrizeEmps)


"""
如果公司年会抽奖的时候，奖项和中奖人数不变，抽奖箱中的员工并不是唯一的呢：入职一年内的员工在抽奖箱中有一个对应的员工牌，
入职两年的有两个……（目的是增加老员工的中将概率）；
"""

# empList = [list(range(300))]
# for empCd in empList:
#     while empList.count(empCd) > 1:
#         for i in range(empList.count(empCd)):
#             empList.remove(empCd)  # 员工工号数量就是循环次数；循环遍历列表，每次循环会remove移除第一个

