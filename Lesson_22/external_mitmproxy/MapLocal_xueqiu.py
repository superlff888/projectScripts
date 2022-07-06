# -*- coding=utf-8 -*-

# =============================================================

from mitmproxy import http


"""
1、同一字符，不同编码规则编码后，得到的二进制数字可能有差异
2、encoding编解码器（底层自动执行编码和解码） == decode解码 + encode编码
2、notepad++中的编码规则为utf-8,而open函数默认gbk编解码规则，open函数用GBK解码了被UTF-8编码的文件（前者用两个字节表示一个汉字而后者用三个），
   因不同编码规则得到的二进制数字可能有差异，所以我们必须先人为用同一规则utf-8对文件数据逆向解码，然后用gbk规则重新编码
"""


def request(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url:
        # 打开本地数据文件; encoding默认gbk编解码器（底层自动执行编码和解码），即默认gbk解码对应文件（可用decode方法修改解码规则）
        with open(r"C:\Users\HouseLee\Desktop\mapLocal.json", mode="rb+") as f:  # mode="rb+"或者 encoding = "utf-8"
            flow.response = http.Response.make(
                200,
                # 读取本地文件中的数据作为响应内容;
                # notepad++中编码格式为utf-8,而open函数默认gbk编解码器'gbk' codec can't decode byte 0xbc,既然gbk不能解码byte 0xbc，那就人工转为utf-8解码
                f.read().decode("utf-8").encode("gbk"),  # 先人为将gbk转化为utf-8对读取的二进制字符进行解码,再用gbk的模式对字符（汉字）进行进行编码
                {"Content-Type": "application/json",
                 "myHeader": "lee"}
            )


"""
def request(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url:
        # encoding = "utf-8" ，即人工转为utf-8编解码器，open函数的文件数据逆向解码规则也为utf-8
        with open("C:\\Users\\HouseLee\\Desktop\\mapLocal.json", encoding = "utf-8") as f:   # 打开本地数据文件
            flow.response = http.Response.make(
                200,
                # 读取本地文件中的数据作为响应内容（本地文件含中文）
                f.read().encode("gbk"),  # open函数参数一设置解码规则，所以此处仅用gbk的模式对字符进行进行编码即可（中文编码格式为gbk）
                {"Content-Type": "application/json",
                 "myHeader": "lee"}
            )
"""

