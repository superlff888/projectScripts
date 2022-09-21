# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:24
# @Author  : ╰☆H.俠ゞ
# =============================================================

from CTTQ.dcsqas.web.base.base_page import BasePage


class GateAIServer_machineVision(BasePage):
    """机器视觉"""
    def gateAIServer_machineVision(self, obj):
        """
        obj  列表或元组
        by_*  列表或元组
        by   列表或元组
        locator   列表或元组
        """
        by, locator = obj
        self.clicked(by, locator)

    def identity_card(self, obj):
        """身份证"""
        by, locator = obj
        self.clicked(by, locator)
        return

    def verificationCode(self, obj):
        """验证码"""
        by, locator = obj
        self.clicked(by, locator)
        return

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


class Phonetic_language:
    """语音语言"""
    def Keyword_extraction(self, obj):
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

    def phonetic_language(self):
        """语音语言"""
        pass


class GateAIServer300:

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


class GateAIServer400:

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


class GateAIServer500:

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


class GateAILink:
    def gateAILink(self, obj):
        pass