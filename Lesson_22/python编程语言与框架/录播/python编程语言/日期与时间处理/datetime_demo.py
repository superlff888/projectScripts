# @Time  : 2022/02/12 19:03
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import datetime

# 获取当前时间
now = datetime.datetime.now()
print(f'当前时间为：{now}')

# 将时间转化为字符串
now_strf = now.strftime('%Y%m%d %H:%M:%S')
print(now_strf)
# 将字符串转化为datetime实例
now_strp = now.strptime(now_strf, '%Y%m%d %H:%M:%S')
print(now_strp)
# 将时间转化为字符串
result = now_strp.strftime(f'%a %b %d日  %H:%M:%S')  # 周  月  日
print(result)


"""
时间与时间戳相互转换
"""

mtp = 16932759.3478
s = datetime.datetime.fromtimestamp(mtp)  # 时间戳转化为时间
print(s)

print(s.timestamp())  # 将时间转化为时间戳

