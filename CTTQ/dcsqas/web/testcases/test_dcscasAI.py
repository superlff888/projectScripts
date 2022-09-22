# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import unittest
import pytest
from selenium.webdriver.common.by import By

from CTTQ.dcsqas.web.Utils.tools import yaml_parse
from CTTQ.dcsqas.web.gateCenterAI.login_dcs import Login


class TestCas(unittest.TestCase):

    # 机器视觉
    @pytest.mark.parametrize('url,obj', yaml_parse("./m.yml")["login"])
    def setup_class(self, url, obj):
        self.lg = Login(url=url)
        self.lg.win_max()
        self.gmv, self.pl, self.gl = self.lg.login(obj)
        self.lg.implicitly_time(3)

    @pytest.mark.parametrize('obj, value, by_card, timeout, ele, by_text', yaml_parse("./m.yml")["ID"])
    def test_IDci(self, obj: tuple, value, by_card: tuple, timeout, ele: tuple, by_text: tuple):
        self.gmv.identity_card(obj).ID_card_identification(value, by_card)
        self.lg.WebDriverWait_until_clickable(timeout, ele)
        text = self.lg.get_text(by_text)
        self.assertIn(text, ("姓名", "身份证"))

    @pytest.mark.parametrize('obj, value, by_card, timeout, ele, by_text', yaml_parse("./m.yml")["vc"])
    def test_vc(self, obj: tuple, value, by_card: tuple, timeout, ele: tuple, by_text: tuple):
        self.gmv.verificationCode(obj).verificationCode_identification(value, by_card)
        self.gl.WebDriverWait_until_clickable(timeout, ele)
        text = self.lg.get_text(by_text)
        self.assertEqual(text, "验证码")

    def test_pd(self):
        pass

    def test_hpe(self):
        pass

    def test_crO(self):
        pass

    def test_ist(self):
        pass

    # 语音语言
    @pytest.mark.parametrize('obj, value, by_key, by_c, timeout, ele, by_text', yaml_parse("./m.yml")["ke"])
    def test_ke(self, obj: tuple, value, by_key: tuple, by_c: tuple, timeout, ele: tuple, by_text: tuple):
        self.pl.keyword_extraction(obj).keyword_extraction(value, by_key, by_c)
        self.gl.WebDriverWait_until_clickable(timeout, ele)
        text = self.lg.get_text(by_text)
        self.assertIn(text, ("关键字1", "关键字2", ))

    @pytest.mark.parametrize('obj, value, by_summary, by_c, timeout, ele, by_text', yaml_parse("./m.yml")["summary"])
    def test_ts(self, obj: tuple, value, by_summary: tuple, by_c: tuple, timeout, ele: tuple, by_text: tuple):
        self.pl.text_summary(obj).text_summary(value, by_summary, by_c)
        self.gl.WebDriverWait_until_clickable(timeout, ele)
        text = self.lg.get_text(by_text)
        self.assertIn("文本摘要", text)

    @pytest.mark.parametrize('obj, value_title, by_title, by_content, value_content, by_c, timeout, ele, by_text',
                             yaml_parse("./m.yml")["oa"])
    def test_oa(self, obj: tuple, value_title, by_title: tuple, by_content: tuple, value_content, by_c: tuple,
                timeout, ele: tuple, by_text: tuple):
        self.pl.opinion_analysis(obj).opinion_analysis(value_title, by_title, by_content, value_content, by_c)
        self.gl.WebDriverWait_until_clickable(timeout, ele)
        text = self.lg.get_text(by_text)
        self.assertIn("舆情分析正面", text)

    # def test_tec(self, obj: tuple, value, by_err: tuple, by_c: tuple, timeout, ele: tuple, by_text: tuple):
    #     self.pl.text_error_correction(obj).text_error_correction(value, by_err, by_c)
    #     self.gl.WebDriverWait_until_clickable(timeout, ele)
    #     text = self.lg.get_text(by_text)
    #     self.assertEqual("", text)

    @pytest.mark.parametrize('obj, value_t1, by_t1, value_t2, by_t2, by_c, timeout, ele, by_text',
                             yaml_parse("./m.yml")["sc"])
    def test_sc(self, obj: tuple, value_t1, by_t1: tuple, value_t2, by_t2: tuple, by_c: tuple,
                timeout, ele: tuple, by_text: tuple):
        self.pl.similar_content(obj).similar_content(value_t1, by_t1, value_t2, by_t2, by_c)
        self.gl.WebDriverWait_until_clickable(timeout, ele)
        text = self.lg.get_text(by_text)
        self.assertIn("相似度", text)

    # def test_ar(self, obj: tuple, value, by_addr: tuple, by_c: tuple, timeout, ele: tuple, by_text: tuple):
    #     self.pl.address_recognition(obj).address_recognition(value, by_addr, by_c)
    #     self.gl.WebDriverWait_until_clickable(timeout, ele)
    #     text_list = self.lg.get_text(by_text)
    #     self.assertListEqual("", text_list)

    # def test_sr(self):
    #     self.pl.speech_recognition().speech_recognition()

    # def test_ss(self):
    #     self.pl.speech_synthesis().speech_synthesis()


if __name__ == "__main__":
    os.system("pytest -sv test_dcscasAI.py")
