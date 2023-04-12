# -*- coding=utf-8 -*-
# @Time    : 2022/09/03 14:24
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import random
import webbrowser

import jsonpath
from locust import HttpUser, task, TaskSet, between, constant, FastHttpUser


# locust中的client会自动帮我们处理cookies。类似request.session(),所以如果我们登陆的时候，只需要在on_start中登陆一次就可以了

# 如果在locust中，如果url是不需要统计，则我们不要用clent去访问api，应该用request去访问，这样就locust就不会统计request库发起的请请求
# 指定一个任务集
class My_task_set(TaskSet):
    username = ["zhang", "admin", "hello", "lee"]
    # TOKEN = None

    def on_start(self):
        data = {'userName': 'admin', 'password': '1234'}
        userName = random.choice(My_task_set.username)
        data['userName'] = userName
        My_task_set.username.remove(userName)
        if len(self.username) == 0:
            exit(0)  # 退出
        with self.client.post("/pinter/bank/api/login2", data=data, name="登录", catch_response=True) as res:
            if res.json()["code"] == "0":
                self.TOKEN = jsonpath.jsonpath(res.json(), "$.data")[0]
                print(self.TOKEN)
                res.success()
            else:
                res.failure(res.json())

    # 添加初始化方法
    # def on_start(self):
    #     """内置cookie处理"""
    #     print("类似类中的构造方法，【每个用户】在任务开始前，只执行一次,在这里可以定义一个对象的属性，这样其它测试集就可以使用这个属性")
    #     data = {'userName': 'admin', 'password': '1234'}
    #     with self.client.post("/pinter/bank/api/login", data=data, name="登录", catch_response=True) as res:
    #         if res.json()["code"] == "0":
    #             res.success()
    #         else:
    #             res.failure(res.json())

    def on_stop(self):
        print("类似类中的后置方法，每个用户在任务开始后，只执行一次,在这里可以定义一个对象的属性，这样其它测试集就可以使用这个属性")

    # @task(50)
    # def query(self):
    #     """内置cookie处理"""
    #     with self.client.get("/pinter/bank/api/query?userName=admin", name='银行余额查询',
    #                          verify=False, catch_response=True) as res:
    #         if res.json()['code'] == '0':
    #             res.success()
    #         else:
    #             res.failure(res.json())\

    @task
    def query2(self):
        """token需要关联"""
        headers = {"testfan-token": self.TOKEN}  # 实例属性方式 传递参数
        with self.client.get("/pinter/bank/api/query2?userName=admin", headers=headers, name='银行余额查询',
                             verify=False, catch_response=True) as res:
            if res.json()['code'] == '0':
                res.success()
            else:
                res.failure(res.json())

    # 这是某个任务,30是比例，比如这里是30/50
    @task
    def get_sku(self):
        # client就是个requests对象
        # catch_response为True可以自定义请求是否成功；verify如果为True 则https 请求会校验证书
        with self.client.get("/pinter/com/getSku?id=1", name='获取商品id', verify=False, catch_response=True) as res:
            print(res.json())
            if res.json()["code"] == "0":
                res.success()
            else:
                res.failure("ff")


class WebSite(FastHttpUser):  # mac 可发5000并发； win 1024(句柄限制)
    # 被测系统的host（接口url）
    host = 'http://82.156.74.26:9088'
    # 指定要执行哪个任务集
    # task_set = My_task_set
    # task_set = task(My_task_set)
    tasks = [My_task_set, ]
    wait_time = between(1, 2)  # 单位：秒
    # # 请求和请求之间最小的间隔时间
    # min_wait = 100
    # # 请求和请求之间最大的间隔时间
    # max_wait = 2000

    # constant固定用户前后操作时间为3秒
    # wait_time = constant(3)  # 思考时间(线上时，可去掉，模拟高压)


# Number of total users to simulate   模拟的用户数
# Spawn rate                          每秒产生的用户数


if __name__ == '__main__':
    # 控制浏览器打开locust页面
    webbrowser.open_new_tab('http://localhost:8089')
    # 控制cmd执行locust，“MyTaskSet.py”为需要运行py脚本名字，“http://82.156.74.26:9088”为压测服务器地址; --headless 后台执行,无web界面
    # -u 用户数 -r 每秒启动用户数  -t 运行时间  --csv 测试结果保存在csv文件中  --stop-timeout=60  停止延迟时间(防止突然停止，造成请求错误)
    os.system("locust -f MyTaskSet.py -u 2 -r 1 -t 1h30m20s --csv=result --stop-timeout=60")

"""
【指标计算】
1、1M bit=1/8M bytes=128K bytes   ==>  1000M宽带也就是  1000/8=125M bytes  也就是说下载速度理论上最大能达到每秒125M bytes
2、TPS：服务器每秒钟处理的事务数
3、响应时间预期指标：2，5，8原则
4、标准错误率：99.9%，核心业务：99.99%，普通业务99%

【关联】
 1、cookie处理：登录接口返回的cookie不用单独提取后关联下游接口，只需要放在on_start中
 2、token处理：类属性或实例属性传递token；注意，并发用户名应不同，否则会造成token覆盖
"""
