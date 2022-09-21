# -*- coding=utf-8 -*-
# @Time    : 2022/09/21 11:24
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""机器视觉"""
from selenium.webdriver.common.by import By

from CTTQ.dcsqas.web.base.base_page import BasePage


class Identity_card(BasePage):
    def ID_card_identification(self, value, by):
        """*by"""
        self.send_file(value, by)  # 上传图片


class VerificationCode(BasePage):
    def verificationCode_identification(self, value, by):
        """by is a tuple"""
        self.send_file(value, by)  # 上传图片


class Pedestrian_detection(BasePage):
    def pedestrian_detection(self):
        pass


class Human_posture_estimation(BasePage):
    def human_posture_estimation(self):
        pass


class Character_recognition_OCR(BasePage):
    def character_recognition_OCR(self):
        pass


class Image_style_transfer(BasePage):
    def image_style_transfer(self):
        pass