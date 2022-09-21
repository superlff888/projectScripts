# -*- coding=utf-8 -*-
# @Time    : 2022/09/21 11:25
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""语音语言"""
from CTTQ.dcsqas.web.base.base_page import BasePage


class Keyword_extraction(BasePage):
    def keyword_extraction(self, value, by_s, by_c):
        self.send(value, by_s)
        self.clicked(by_c)


class Text_summary(BasePage):
    def text_summary(self, value, by_s, by_c):
        self.send(value, by_s)
        self.clicked(by_c)


class Opinion_analysis(BasePage):
    def opinion_analysis(self, value_title, by_title, by_content, value_content, by_c):
        self.send(value_title, by_title)
        self.send(value_content, by_content)
        self.clicked(by_c)


class Text_error_correction(BasePage):
    def text_error_correction(self, value, by_s, by_c):
        self.send(value, by_s)
        self.clicked(by_c)


class Similar_content(BasePage):
    def similar_content(self, value, by_t1, by_t2, by_c):
        self.send(value, by_t1)
        self.send(value, by_t2)
        self.clicked(by_c)


class Address_recognition(BasePage):
    def address_recognition(self):
        pass


class Speech_recognition(BasePage):
    def speech_recognition(self):
        pass


class Speech_synthesis(BasePage):
    def speech_synthesis(self):
        pass
