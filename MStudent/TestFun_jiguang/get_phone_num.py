# -*- coding=utf-8 -*-
# @Time    : 2023/04/19 00:13
# @Author  : ╰☆H.俠ゞ
# =============================================================
import random


def get_phone_num():
    # 手机号码总共11位，前三位需要满足具体运营商，后8位可以随意组合
    # firstThreeNumber = ["134", "135", "136", "137", "138", "139", "147", "150", "152", "157", "158",
    #                     "159", "172", "178", "182", "183", "184", "187", "188", "198", "130", "131", "132", "145",
    #                     "155",
    #                     "156", "166", "171", "175", "176", "185", "186", "166", "133", "149", "153", "173", "177",
    #                     "180", "181",
    #                     "189", "199"]
    second_spot = random.choice([3, 4, 5, 7, 8])  # dict中的key
    third_spot = {3: random.randint(0, 9),
                  4: random.choice([5, 7, 9]),
                  5: random.choice([i for i in range(10) if i != 4]),
                  7: random.choice([i for i in range(10) if i not in [4, 9]]),
                  8: random.randint(0, 9)}[second_spot]
    remain_spot = random.randint(10000000, 99999999)
    phone_num = f"1{second_spot}{third_spot}{remain_spot}"
    return phone_num

