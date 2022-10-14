# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 22:50
# @Author  : ╰☆H.俠ゞ
# =============================================================


class ContextBase:
    _context = None

    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context