# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:24
# @Author  : ╰☆H.俠ゞ
# =============================================================

from CTTQ.dcsqas.web.base.base_page import BasePage
from CTTQ.dcsqas.web.gateCenterAI.machine_vision import Identity_card, VerificationCode


class GateAIServer_machineVision(BasePage):
    """机器视觉"""
    def gateAIServer_machineVision(self, obj):
        """
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
        pass

    def human_posture_estimation(self):
        """人体姿态估计"""
        pass

    def character_recognition_OCR(self):
        """文字识别OCR"""
        pass

    def image_style_transfer(self):
        """图像风格迁移"""
        pass


class Phonetic_language(BasePage):
    """语音语言"""
    def keyword_extraction(self, obj):
        """关键词提取"""
        pass

    def text_summary(self):
        """文本摘要"""
        pass

    def opinion_analysis(self):
        """舆情分析"""
        pass

    def text_error_correction(self):
        """文本纠错"""
        pass

    def similar_content(self):
        """相似内容推荐"""
        pass

    def address_recognition(self):
        """地址识别"""
        pass

    def speech_recognition(self):
        """语音识别"""
        pass

    def speech_synthesis(self):
        """语音合成"""
        pass

    def phonetic_language(self, obj):
        """语音语言"""
        """
        by   定位方式
        locator   元素
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
    def gateAILink(self, obj):
        pass