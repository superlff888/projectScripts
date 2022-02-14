# @Time  : 2022/01/26 22:25
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
def logging(func):  # 定义一个参数func，用来接收自动传过来的原函数对象
    print(f'the time of {func.__name__} is coming!')
    return func


def logg(func):  # 定义一个参数func，用来接收自动传过来的原函数对象
    print(f'the time of {func.__name__} is coming!')
    func()
    print(f'the time of {func.__name__} is over!')
    return func
