# -*- coding=utf-8 -*-
# @Time    : 2022/09/21 16:17
# @Author  : ╰☆H.俠ゞ
# =============================================================
import base64
import importlib
import io
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


# a = image_to_base64(r"C:\Users\HouseLee\Desktop\验证码3.png", "base64", "b64encode")
# base64_to_image("1.jpg", a)