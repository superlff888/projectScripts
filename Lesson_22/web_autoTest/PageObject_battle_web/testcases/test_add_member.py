# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
from hamcrest import *

from Lesson_22.web_autoTest.PageObject_battle.page_object.main_page import MainPageObject


class TestAddMember:
    def setup_class(self):
        """
        用例执行前的准备工作： 对象的初始化
        在一条case 当中，尽量就使用同一个url。
        """
        self.main = MainPageObject()
        # self.contact = ContactPage()
        self.main.login()  # 子类调用父类的方法
        # self.contact.login()

    def teardown_class(self):
        """
        退出driver 进程
        :return:
        """
        self.main.driver.quit()
        # self.contact.driver.quit()

    def teardown(self):
        """
        保证每一条用例开始的时候，执行状态是正确。
        回复到用例的初始页面
        :return:
        """
        self.main.back_start_page()

    # 数据清理的两种方式：
    # 1. 在teardown/teardown_class 即为每条用例执行之后，清理用例数据。
    # 2. setup_class的时候清理数据。保证自动化测试用例在执行过程中，有一个比较干净的数据环境 【推荐】
    # 在UI自动化测试中，测试的前置后置动作，不一定要通过UI的方式完成。
    # 建议大家使用稳定的方式去完成。比如通过接口去做数据清理（关联表不熟悉的话）。

    def test_add_member(self):
        # 1. 点击添加成员，跳转到添加成员页面
        # 2. add member 的操作
        # 3. 获取通讯录页面的成员列表（实际结果）
        name = "伊泽瑞尔4"
        mem_list = self.main. \
            goto_add_member_page(). \
            add_member(name, "010442", "18900112222"). \
            get_member_list()

        # self.main.goto_add_member_page().
        # 4 断言 实际结果也就是成员列表 是否符合预期
        assert name in mem_list

    def test_add_member_fail(self):
        """
        当手机号码格式输入错误，有没有错误提示
        :return:
        """
        name = "伊泽瑞尔5"
        res = self.main.goto_add_member_page().add_member_fail(name, "0101233", "009")
        assert "请填写正确的手机号码" in res  # 断言：实例结果也就是成员列表是否符合预期
        # assert_that(res, equal_to("请填写正确的手机号码"), "电话号码输入错了")
