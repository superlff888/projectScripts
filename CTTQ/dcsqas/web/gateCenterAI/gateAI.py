# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:24
# @Author  : ╰☆H.俠ゞ
# =============================================================
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait

from CTTQ.dcsqas.web.base.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC


class GateAI(BasePage):

    def search(self, obj):
        """
        obj  列表或元组
        by_*  列表或元组
        by   列表或元组
        locator   列表或元组
        """
        by_send, text, by_click = obj

        # 可以关闭按钮时，关闭弹框
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
        # self.fond(close_bn).click()
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_send))  # 等待输入框可点击
            self.fond(by_send).send_keys(text)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_click))  # 等待检索框可点击

            # WebDriverWait(self.driver, 20).until(text == "华为")  # 等待检索框可点击
            self.fond(by_click).click()
            self.driver.implicitly_wait(2)
        except NoSuchElementException:
            return self.search(obj)
        except ElementClickInterceptedException:
            return self.search(obj)
        except WebDriverException:
            return self.search(obj)
        except ElementNotVisibleException:
            return self.search(obj)
        except Exception as e:
            print(f"抛出异常{e}")
            return self.search(obj)

    # def miss(self, close_bn):
    #     try:
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
    #         self.fond(close_bn).click()
    #         self.fond(close_bn)
    #         return self.search, self.fond, self.driver
    #     except ElementClickInterceptedException:
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
    #         return self.miss(close_bn)
    #     except Exception:
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
    #         return self.miss(close_bn)

