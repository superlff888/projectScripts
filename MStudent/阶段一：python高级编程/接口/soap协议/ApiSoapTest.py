# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-11-06
desc: 
sample: 
"""
import random
import re

import pytest
import requests


class TestSoap:
    host = 'http://ws.webxml.com.cn'

    def setup(self):
        firstThreeNumber = ["134", "135", "136", "137", "138", "139", "147", "150", "152", "157", "158",
                            "159", "172", "178", "182", "183", "184", "187", "188", "198", "130", "131", "132", "145",
                            "155",
                            "156", "171", "175", "176", "185", "186", "166", "133", "149", "153", "173", "177",
                            "180", "181",
                            "189", "199"]
        phone = random.choice(firstThreeNumber) + str(random.randint(10000000, 99999999))
        self.phone = phone

    def test_soap2(self):
        print(self.phone)

    # @pytest.mark.parametrize('phone', getParametrizeList("phone.csv",False))
    def test_soap(self):  # (self, phone)
        print(self.phone)
        url = self.host + '/WebServices/MobileCodeWS.asmx'
        xml_data = '<?xml version="1.0" encoding="utf-8"?>' \
                   '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' \
                   'xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">' \
                   '<soap:Body><getMobileCodeInfo xmlns="http://WebXml.com.cn/">' \
                   f'<mobileCode>{self.phone}</mobileCode><userID></userID>' \
                   '</getMobileCodeInfo></soap:Body></soap:Envelope>'
        headers = {'Content-Type': 'text/xml; charset=utf-8'}
        rep = requests.post(url=url, data=xml_data, headers=headers)
        print(rep.text)
        result = re.findall(r'<getMobileCodeInfoResult>(.+?)</getMobileCodeInfoResult>', rep.text)
        print(result)
        result_str = result[0]
        print(result_str)
        if result_str != "没有此号码记录":
            result_str_value = result_str.split('：')[1]
            result_str_value_last = result_str_value.split(" ")[-1]
            print(result_str_value_last)
        else:
            print("没有此号码记录")
            # self.test_soap()
