# -*- coding=utf-8 -*-
# @Time    : 2023/02/17 11:52
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# 创建options
from common.driver import element_click_success, element_send_success

options = webdriver.ChromeOptions()
# 添加静默参数
options.add_argument('headless')
print("初始化driver")
# 以静默方式初始化浏览器驱动，启动浏览器
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.implicitly_wait(10)


def login():
    print("打开shop登录首页")
    driver.get("http://www.mtxshop.com:3000/login")
    sleep(1)
    driver.maximize_window()
    driver.find_element(By.PARTIAL_LINK_TEXT, '账号登录').click()
    sleep(1)
    # driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[@id='username' and @placeholder='邮箱/用户名/已验证手机']").send_keys("leeseller")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456")
    driver.find_element(By.XPATH, "//*[@id='validcode']").send_keys("1512")
    driver.find_elements(By.XPATH, "//*[@class='form-sub']")[1].click()  # 登录


def center():  # 进入个人中心
    locator = (By.XPATH, "//*[@class='to-member' and text()='进入个人中心']")
    print(WebDriverWait(driver, 10, 0.1).until(ec.presence_of_element_located(locator)))
    WebDriverWait(driver, 10, 0.1).until(element_click_success(*locator))


def receive_address():
    driver.find_element(By.XPATH, "//*[text()='收货地址' and @href='/member/shipping-address']").click()
    # driver.find_element(By.XPATH, "//*[@class='el-button add-address-btn el-button--default el-button--mini']").click()
    # driver.find_element(By.CSS_SELECTOR, "#shipping-address button[class='el-button add-address-btn el-button--default el-button--mini']").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".el-button.add-address-btn.el-button--default.el-button--mini").click()  # CSS定位 空格用.填充


def add_address():
    driver.find_element(By.CSS_SELECTOR, ".el-form>div:first-child .el-input__inner").send_keys("lee")  # 父子级 爷孙级
    driver.find_element(By.CSS_SELECTOR, ".el-form>div:nth-child(2) .el-input__inner").send_keys(
        "15715151020")  # 父子级 爷孙级
    # 收货地区
    ele = driver.find_element(By.CSS_SELECTOR, ".app-address-title>.app-address-title-view")
    action = ActionChains(driver)
    action.move_to_element(ele).perform()
    ele = driver.find_element(By.XPATH, "//*[@class='app-address-area-a' and text()='上海']")
    WebDriverWait(driver, 10, 0.1).until(ec.element_to_be_clickable(ele))
    ele.click()
    driver.find_element(By.LINK_TEXT, "黄浦区").click()
    driver.find_element(By.LINK_TEXT, "城区").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .el-input__inner").send_keys("金山屯行政村")
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .el-input__inner").send_keys("金山屯")
    # driver.find_element(By.CLASS_NAME, "el-checkbox__label").click()  # 设置默认地址
    driver.find_element(By.CSS_SELECTOR, ".layui-layer-btn0").click()


def del_address():
    driver.find_element(By.CSS_SELECTOR, "tr:first-child .el-button.delete-btn.el-button--text.el-button--mini").click()
    driver.find_element(By.XPATH, "//*[@class='layui-layer-btn0' and text()='确定']").click()


def person_info():
    # ele = (By.CSS_SELECTOR, ".menu-item>.nuxt-link-exact-active.nuxt-link-active")  # 单选框不能点击
    ele = (By.PARTIAL_LINK_TEXT, "个人信息")
    WebDriverWait(driver, 10, 0.1).until(element_click_success(ele))  # True的同时做了点击"个人信息"操作
    # 上传头像  -> send_keys方法传递图片仅限input标签
    # driver.find_element(By.CLASS_NAME, "eidt-mask").click()
    WebDriverWait(driver, 10, 0.1).until(
        element_send_success(r"C:\Users\HouseLee\Desktop\snipaste.png", By.NAME, "file"))
    sleep(3)
    WebDriverWait(driver, 10, 0.1).until(element_click_success(By .XPATH, "//*[text()='确 定']"))

    driver.find_element(By.CSS_SELECTOR, ".el-form>div:nth-child(2) .el-input__inner").clear()  # 清空昵称输入框
    driver.find_element(By.CSS_SELECTOR, ".el-form>div:nth-child(2) .el-input__inner").send_keys("lee")  # 昵称
    driver.find_element(By.CSS_SELECTOR, ".el-radio.is-checked .el-radio__label").click()  # 性别
    js = 'document.getElementsByClassName("el-input__inner")[1].removeAttribute("readonly")'
    driver.execute_script(js)  # 去除生日框的只读属性
    driver.find_element(By.XPATH, "//*[contains(@class,'el-date-editor el')]/input[@class='el-input__inner']"). \
        send_keys("1999-11-16")
    sleep(2)
    driver.find_element(By.XPATH, "//*[text()='详细地址']/..//input[@class='el-input__inner']").click()  # 点击该输入框，用于【关闭日期控件弹框】
    driver.find_element(By.XPATH, "//*[text()='详细地址']/..//input[@class='el-input__inner']").send_keys("云龙山")
    driver.find_element(By.XPATH, "//*[text()='保存资料']")


def search_shop():
    driver.find_element(By.CLASS_NAME, "search-input").clear()
    driver.find_element(By.CLASS_NAME, "search-input").send_keys()
    driver.find_element(By.CLASS_NAME, "search-btn shop").click()


def choose_goods_buyNow():
    driver.find_element(By.CLASS_NAME, "search-input").clear()
    WebDriverWait(driver, 10, 0.1).until(element_send_success("李小兵", By.CSS_SELECTOR, ".search-input"))
    WebDriverWait(driver, 10, 0.1).until(element_click_success(By.CSS_SELECTOR, ".search-btn.shop"))
    WebDriverWait(driver, 10, 0.1).until(element_click_success(By.XPATH, "//*[@href='/goods/19813']"))  # 窗口跳转
    handles = driver.window_handles
    print(f"获取窗口句柄{handles}")

    # # 直接切换到最新窗口
    # driver.switch_to.window(handles[-1])

    url = driver.current_url
    for handle in handles:
        driver.switch_to.window(handle)
        if handle.title() == "电视机-码同学实战项目":
            print(f'窗口标题：{handle.title()}')
            break
        # driver.switch_to.window(handle)
        # if url == "http://www.mtxshop.com:3000/goods/19813":
        #     break

    WebDriverWait(driver, 10, 0.1).until(element_click_success(By.CSS_SELECTOR, ".buy-btn.buy"))
    # 订单备注
    WebDriverWait(driver, 10, 0.1).until(
        element_send_success("请尽快发货", By.CSS_SELECTOR, ".bottom-ckt-inventory .el-input__inner"))
    WebDriverWait(driver, 10, 0.1).until(element_click_success(By.CLASS_NAME, "bill_btn"))


def fresh():
    driver.refresh()


def closed():
    sleep(3)
    driver.close()  # 关闭当前窗口
    print("关闭浏览器")


def quit_chrome():
    driver.quit()


if __name__ == '__main__':
    login()
    center()
    person_info()
    closed()
