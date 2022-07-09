# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 15:10
# @Author  : ╰☆H.俠ゞ
# =============================================================

from requests_xml import XMLSession

"""
XML断言
"""


def test_xml():
    session = XMLSession()  # 生产一个session,用于消耗性会话
    # 该请求url可能有问题，所以有标黄警告
    r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')  # 发起xml请求
    print(r.content)
    print(r.xml.links)
    print(r.xml)  # 获取xml的层次结构
    # XPath is the main supported way to query an element (learn more):
    print(r.xml.xpath('//item', first=True))  # 取item的文字可以是r.xml.xpath('//item', first=True).text
# ['http://www.nasa.gov/image-feature/from-the-earth-moon-and-beyond',
# 'http://www.nasa.gov/image-feature/jpl/pia21974/jupiter-s-colorful-cloud-belts',
# 'http://www.nasa.gov/',
# 'http://www.nasa.gov/image-feature/portrait-of-the-expedition-54-crew-on-the-space-station', ...] #<Element 'item' >
