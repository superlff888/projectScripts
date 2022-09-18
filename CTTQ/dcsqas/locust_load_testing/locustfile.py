# -*- coding=utf-8 -*-
# @Time    : 2022/09/03 10:36
# @Author  : ╰☆H.俠ゞ
# ========================================================
import os
from time import sleep

from locust import HttpUser, between, task, TaskSet
import pytest
from selenium.webdriver.common.by import By
import sys

sys.path.append(f"D:\\Develop\\git_pub_repositories\\projectScripts")  # （运行程序时）添加path环境变量
from CTTQ.dcsqas.page_object.login_dcs import Login


class UserBehave(TaskSet):

    def on_start(self):
        self.lg = Login(url="https://ainewqas.cttq.com/cvue/SunnyShop-WebPC")
        self.lg.win_max()
        self.searched, self.fond, self.driver_ = self.lg.login([(By.ID, "login-workcode"), "8106139",
                                                                (By.ID, "login-password"), "cttq.1234",
                                                                (By.ID, "login-btn")]) \
            .miss((By.XPATH, "//div[@class='el-dialog__body']/div[3]"))  # 关闭提示框

    @task(1)  # 添加task装饰器，性能测试才会执行该任务；也可以task(3)按百分比指定权重，比如线程为9，那么该任务权重为 9*（3/N）
    def search(self):
        self.searched([(By.XPATH, "//input[@placeholder='请输入商品名、品牌、CAS号、货号']"), "华为",
                       (By.XPATH,
                        "//div[@class='el-input-group__append']/button[@class='el-button el-button--default']")])
        self.driver_.implicitly_wait(1)
        self.fond((By.XPATH, "//input[@placeholder='请输入商品名、品牌、CAS号、货号']")).clear()  # 清空单元格
        # 获取商品名列表
        assert 1 == 1


class WebSiteUser(HttpUser):
    # 【思考时间】设置一个随机时间间隔
    wait_time = between(3, 5)
    tasks = [UserBehave]
    host = "https://mallqas.cttq.com"


if __name__ == "__main__":
    os.system("locust")
