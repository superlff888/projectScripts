# @Time  : 2021/05/20 14:06
# @Author    : House Lee
# -*-coding=utf-8-*-

import re

"""
.  点表示匹配任意一个字符，一个"."对应一个字符
a   12a1a1a

'\w\s+\d[1-3]*\w..'

"""

# print(re.search(r'^\w[a-zA-Z\_]+\d{6}', 'aq_12343456'))
#
# print(re.match(r'^\d{3}\-\d{3,8}$', '010----12345'))

# print(re.match(r'\Aabc', 'abc123'))
# print(re.match('123\Z', '123123'))

'''
强烈建议使用Python的r前缀，就不用考虑转义的问题了
注意："*"表示任意“个”，表示的是个数，而不是任意字符
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m
个字符；[az]代表字符类型范围
'''

# re.search('\w\s+\d[1-3]+', 'a   12a')
#
# test = input('用户输入的字符串:')
# if re.match(r'\w\s+\d[1-3]+', test):
#     print('ok')
# else:
#     print('failed')

'''
切分字符串
'''
# print(re.split(r'\s+', 'a b   c'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
# print(f'\n')

'''
分组
'''

print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').group())
print(re.findall(r'a(.+)b', 'ba123ba678ba11111111'))


'''
编译
'''
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#
# print(re_telephone.match('010-12345').groups())
#
# print(re_telephone.match('010-12345'))
