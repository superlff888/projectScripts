# -*- coding=utf-8 -*-
# @Time    : 2023/02/03 14:13
# @Author  : ╰☆H.俠ゞ
# =============================================================
from functools import singledispatch, update_wrapper


def methodispatch(func):
    dispatcher = singledispatch(func)
    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)
    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper