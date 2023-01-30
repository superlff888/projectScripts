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

# print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').group())  # 返回匹配值
# print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').groups())  # 以元组的形式将两组匹配到的值返回
# print(len(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').groups()))
# print(re.findall(r'a(.+)b', 'ba123ba678ba11111111')[0])
# print(re.findall(r'a(.+)b', 'ba123ba678ba11111111b'))


'''
编译：编译成正则表达式对象
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # re_telephone正则表达式对象
print(re_telephone.match('010-12345'))
print(re_telephone.match('010-12345').groups())
print(re.match(re_telephone, '010-12345'))
print(re.match(re_telephone, '010-12345').groups())
print(re.match(re_telephone, '010-12345'))


url = "https://ke.qq.com/webcourse/index.html#cid=3451092&term_id=104315825&taid=12103557145995476&type=1024&vid=387702291472621478"
pattern = r"[#|&]"  # 用 | 或者 & 进行分割
print(re.split(pattern, url))