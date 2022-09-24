# -*- coding=utf-8 -*-
# @Time    : 2022/09/21 16:17
# @Author  : ╰☆H.俠ゞ
# =============================================================
import base64
import importlib
import io
import os

import allure
import yaml
from PIL import Image


def image_to_base64(img_url, module, name):
    """
    :: module: 'base64'
    :: name  : 'b64encode'
    :: usage :
        base64encode 用于base64编码
        base64decode 用于base64解码
        decode 用于解码字节的编码
    :: for example:
        image_to_base64(r'C:\\Users\\HouseLee\\Desktop\\验证码3.png', 'base64', 'b64encode')
    """
    # 动态导入
    b64m = importlib.import_module(module)
    b64encode = getattr(b64m, name)
    with open(img_url, 'rb') as f:  # 二进制方式打开图文件
        b64_encode = b64encode(f.read())  # 读取文件内容，转换为base64二进制编码
        pre_b64_decode = b64_encode.decode()  # decode 用于解码 字节的编码
        b64_decode = f"data:image/png;base64,{pre_b64_decode}"  # 字面量拼接
    return b64_decode


# 打开图片
def open_image(img_b64decode):
    """
    PIL 最常用的图像处理库
    """
    image = io.BytesIO(img_b64decode)  # BytesIO操作二进制数据
    print(image)
    img = Image.open(image)
    img.show()


def base64_to_image(path, base64_str):
    base64_code = base64_str.split(",")[1]
    img_b64_decoded = base64.b64decode(base64_code)
    # open_image(img_b64_decoded)  # 打开图片验证下
    with open(path, 'wb') as png:
        png.write(img_b64_decoded)


def yaml_parse(stream_file):
    with open(stream_file, encoding='utf-8') as f:
        list_ = yaml.load(f)
    return list_


# a = image_to_base64(r"C:\Users\HouseLee\Desktop\验证码3.png", "base64", "b64encode")
# base64_to_image("1.jpg", a)


def shotFromAssertError(func):
    """装饰器功能: 断言错误，会将截图放在allure放到报告中"""
    def wrapper(*args, ** kwargs):  # 接收被装饰函数的参数，self会在args元组的下标1位置
        try:
            func(*args, ** kwargs)
        except AssertionError:
            # 使用时，要将被装饰的函数的body参数放在最后
            allure.attach(body=args[-1], attachment_type=allure.attachment_type.PNG)
    return wrapper