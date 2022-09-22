# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:24
# @Author  : ╰☆H.俠ゞ
# =============================================================

from CTTQ.dcsqas.web.base.base_page import BasePage
from CTTQ.dcsqas.web.gateCenterAI.machine_vision import Identity_card, VerificationCode, Pedestrian_detection, \
    Human_posture_estimation, Character_recognition_OCR, Image_style_transfer
from CTTQ.dcsqas.web.gateCenterAI.phonetic_language import Keyword_extraction, Text_summary, Opinion_analysis, \
    Text_error_correction, Similar_content, Address_recognition, Speech_recognition, Speech_synthesis


class GateAIServer_machineVision(BasePage):
    """机器视觉"""
    def gateAIServer_machineVision(self, obj):
        """
        机器视觉
        by   定位方式
        locator   元素
        """
        by, locator = obj
        self.clicked(by, locator)

    def identity_card(self, obj):
        """身份证"""
        by, locator = obj
        self.clicked(by, locator)
        return Identity_card(self.driver)

    def verificationCode(self, obj):
        """验证码"""
        by, locator = obj
        self.clicked(by, locator)
        return VerificationCode(self.driver)

    def pedestrian_detection(self, obj):
        """行人检测"""
        by, locator = obj
        self.clicked(by, locator)
        return Pedestrian_detection(self.driver)

    def human_posture_estimation(self, obj):
        """人体姿态估计"""
        by, locator = obj
        self.clicked(by, locator)
        return Human_posture_estimation(self.driver)

    def character_recognition_OCR(self, obj):
        """文字识别OCR"""
        by, locator = obj
        self.clicked(by, locator)
        return Character_recognition_OCR(self.driver)

    def image_style_transfer(self, obj):
        """图像风格迁移"""
        by, locator = obj
        self.clicked(by, locator)
        return Image_style_transfer(self.driver)


class Phonetic_language(BasePage):
    """语音语言"""
    def keyword_extraction(self, obj: tuple):
        """关键词提取"""
        by, locator = obj
        self.clicked(by, locator)
        return Keyword_extraction(self.driver)

    def text_summary(self, obj: tuple):
        """文本摘要"""
        by, locator = obj
        self.clicked(by, locator)
        return Text_summary(self.driver)

    def opinion_analysis(self, obj: tuple):
        """舆情分析"""
        by, locator = obj
        self.clicked(by, locator)
        return Opinion_analysis(self.driver)

    def text_error_correction(self, obj: tuple):
        """文本纠错"""
        by, locator = obj
        self.clicked(by, locator)
        return Text_error_correction(self.driver)

    def similar_content(self, obj: tuple):
        """相似内容推荐"""
        by, locator = obj
        self.clicked(by, locator)
        return Similar_content(self.driver)

    def address_recognition(self, obj: tuple):
        """地址识别"""
        by, locator = obj
        self.clicked(by, locator)
        return Address_recognition(self.driver)

    def speech_recognition(self, obj: tuple):
        """语音识别"""
        by, locator = obj
        self.clicked(by, locator)
        return Speech_recognition(self.driver)

    def speech_synthesis(self, obj: tuple):
        """语音合成"""
        by, locator = obj
        self.clicked(by, locator)
        return Speech_synthesis(self.driver)

    def phonetic_language(self, obj: tuple):
        """语音语言"""
        """ 
        by   定位方式 ID XPATH CSS 等等
        locator   定位方式对应的值，如“id”值 u39_state2 , “xpath”值 //*[@id="u39_state2"]
        """
        by, locator = obj
        self.clicked(by, locator)


class GateAIServer300(BasePage):

    def gateAIServer300(self, obj):
        pass

    def gateAIServer301(self):
        pass

    def gateAIServer302(self):
        pass

    def gateAIServer303(self):
        pass

    def gateAIServer304(self):
        pass


class GateAIServer400(BasePage):

    def gateAIServer400(self, obj):
        pass

    def gateAIServer401(self):
        pass

    def gateAIServer402(self):
        pass

    def gateAIServer403(self):
        pass

    def gateAIServer404(self):
        pass


class GateAIServer500(BasePage):

    def gateAIServer500(self, obj):
        pass

    def gateAIServer501(self):
        pass

    def gateAIServer502(self):
        pass

    def gateAIServer503(self):
        pass

    def gateAIServer504(self):
        pass

    def gateAIServer505(self):
        pass

    def gateAIServer506(self):
        pass


class GateAILink(BasePage):
    def fast_api(self, obj: tuple):
        pass

    def modeling_framework(self):
        pass

    def open_community(self):
        pass

    def recommendations(self):
        pass