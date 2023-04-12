# -*- coding=utf-8 -*-
# @Time    : 2023/02/09 14:01
# @Author  : ╰☆H.俠ゞ
# =============================================================


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from common.my_logger import logger


class GlobalDriver:
    driver = None


class InitDriver:
    """
    封装一些和业务无关的重复代码,即底层操作
    r'D:\\Program Files\\Chrome\\Google\\Chrome\\Application'

    """

    def __init__(self, browser='chrome', flag=True):
        """如果flag为False，就静默启动浏览器"""

        if browser.lower() == 'chrome':
            if flag:
                self.driver = webdriver.Chrome()
            else:
                # 创建options
                self.options = webdriver.ChromeOptions()
                # 添加静默参数
                self.options.add_argument('headless')
                # 以静默方式初始化浏览器驱动，启动浏览器
                self.driver = webdriver.Chrome(options=self.options)
        if browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        if browser.lower() == 'ie':
            self.driver = webdriver.Ie()
        elif browser.lower() == 'safari':
            self.driver = webdriver.Safari()
        self.driver.implicitly_wait(18)
        self.driver.maximize_window()
        self.logger = logger
        self.logger.info("初始化driver浏览器驱动")

    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, element_info):
        """
        自定义元素方法，集成了日志和显示等待

        Usage:
            self._driver.find_element({"name": "page操作","type": "定位方式","value": "定位表达式","timeout": "超时时间"})
        returns: element
        """

        obj_name = element_info["name"]
        type = element_info["type"]
        value = element_info["value"]
        timeout = element_info["timeout"]
        locator = self.getBy(element_info)
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
            self.logger.info('查找【{}】使用【{},{}】定位成功'.format(obj_name, type, value))
        except Exception as e:
            self.logger.error('查找【{}】使用【{},{}】定位失败,原因:{}'.format(obj_name, type, value, e))
            raise Exception(f"查找{obj_name}元素，使用【locator:({type},{value})】定位失败,原因：{e}")
        return element

    def getBy(self, element_info):
        """
        return 定位器locator
        """
        type = element_info["type"]
        value = element_info["value"]

        if type.lower() == 'id':
            locator = (By.ID, value)

        elif type.lower() == 'name':
            locator = (By.NAME, value)

        elif type.lower() == 'class':
            locator = (By.CLASS_NAME, value)

        elif type.lower() == 'tag':
            locator = (By.TAG_NAME, value)

        elif type.lower() == 'css':
            locator = (By.CSS_SELECTOR, value)

        elif type.lower() == 'xpath':
            locator = (By.XPATH, value)

        elif type.lower() == 'link_text':
            locator = (By.LINK_TEXT, value)

        elif type.lower() == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, value)
        else:
            raise Exception(f"`{type}`定位方式暂不支持，请更换元素定位方式")
        return locator

    def click(self, element_info):
        """使用自定义方法显示待，直接使用click()方法可能会出现元素拦截，点击交互异常，比如元素拦截"""
        obj_name = element_info["name"]
        type = element_info["type"]
        value = element_info["value"]
        timeout = element_info["timeout"]
        locator = self.getBy(element_info)
        try:
            WebDriverWait(self.driver, timeout).until(element_click_success(locator))
            self.logger.info('查找【{}】使用【{},{}】定位成功'.format(obj_name, type, value))
        except Exception as e:
            self.logger.error('查找【{}】使用【{},{}】定位失败,原因:{}'.format(obj_name, type, value, e))
            raise Exception(f"{obj_name}失败,locator:({type},{value}),原因：{e}")

    def send_key(self, element_info, text):
        """使用自定义方法时间等待"""
        element = self.find_element(element_info)
        element.send_keys(text)

    def clear(self, element_info):
        element = self.find_element(element_info)
        element.clear()

    def send_after_removeAttribute(self, element_info, js, text):
        """
        Usage:
            js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"
            send_after_removeAttribute(js)
        """

        self.driver.execute_script(js)  # 去除生日框的只读属性
        self.send_key(element_info, text)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def move_to_element(self, element_info):
        element = self.find_element(element_info)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def switch_to_window(self, index):
        """切换窗口"""
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])
        self.logger.info(f"【{handles[index].title()}】窗口切换成功")

    def got_screen_shot_as_png(self):
        """返回二进制对象，未储存到文件"""
        return self.driver.get_screenshot_as_png()

    def page_contains_source(self, text):
        """
        用来判断页面元素包含关系

        ::text  : 页面文本信息
        """

        try:
            wait = WebDriverWait(self.driver, timeout=12)  # 提示语是否在12秒内出现
            wait.until(lambda x: text in x.page_source)  # method(self._driver), x代表driver本身
            return True
        except Exception as e:
            self.logger.debug(f"判断页面包含{text}失败的原因：{e}")
            return False

    def is_element_exist(self, element_info):
        """判断元素是否存在"""
        try:
            self.find_element(element_info)
            return True
        except:
            return False


class element_click_success:
    """自定义点击成功,一般放在until中作为call的对象"""

    def __init__(self, by, locator=None):
        self.by = by
        self.locator = locator

    def __call__(self, drivers):  # 在until方法中自动call,即method(self.driver)
        if self.locator is None:
            element = drivers.find_element(*self.by)
            try:
                print(f"元素查找……")
                element.click()
                return True
            except:
                print(f"未找到元素，点击失败")
                return False
        else:
            element = drivers.find_element(self.by, self.locator)
            try:
                element.click()
                print("元素查找并点击")
                return True
            except:
                print('点击异常')
                return False


def move_to_element_success(element_info):
    """既执行鼠标悬浮，又可以放在显示等待时调用until方法，从而运行method(_driver)"""

    def _predicate(_driver):  # until方法会自动传递driver
        element = _driver.find_element(element_info)
        action = ActionChains(_driver)
        action.move_to_element(element).perform()
        return True

    return _predicate


if __name__ == '__main__':
    driver = InitDriver()
    driver.get_url("http://www.mtxshop.com:3000/")
    ele_info = {"name": "登录", "type": "link_text", "value": "登录", "timeout": 8}
    driver.click(ele_info)
