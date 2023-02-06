# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 14:42
# @Author  : ╰☆H.俠ゞ
# =============================================================

import hashlib

def md5(data: str):
    """
    ::file :需要加密的源文件

    MD5为不可逆的加密方法，通过encode(encoding='utf-8')，让其支持utf-8格式进行编码，最后转成十六进制
    """
    return hashlib.md5(data.encode(encoding='utf-8')).hexdigest()

def aes():
    """
    对称加密：加解密算法，需要开发提供私钥，加解密私钥完全相同，所以称为对称算法
    """