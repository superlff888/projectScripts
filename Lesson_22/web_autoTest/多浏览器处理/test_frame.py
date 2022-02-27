# -*- coding=utf-8 -*-
# @Time    : 2022/02/27 10:53
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

from Lesson_22.web_autoTest.多浏览器处理.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')    # 切换到iframe中
        drag = self.driver.find_element_by_id("draggable") # 获取drag元素
        print(drag.text)    # 打印元素的文本信息
        """切换到默认的frame
        方法一：切换到父节点
        方法二：切换到默认frame
        """
        self.driver.switch_to.parent_frame()  # 切换到父节点
        self.driver.switch_to.default_content()  # 切换到默认frame
        print(self.driver.find_element_by_id("submitBTN").text) # 打印点击运行元素的文本
        sleep(3)


"""
命令行参数：
browser=chrome pytest test_frame.py
"""