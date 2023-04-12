# -*- coding=utf-8 -*-
# @Time    : 2022/09/03 14:24
# @Author  : ╰☆H.俠ゞ
# =============================================================

from locust import HttpUser
from locust import task
from locust import TaskSet


# locust中的client会自动帮我们处理cookies。类似request.session(),所以如果我们登陆的时候，只需要在on_start中登陆一次就可以了

# 如果在locust中，如果url是不需要统计，则我们不要用clent去访问api，应该用request去访问，这样就locust就不会统计request库发起的请请求
# 指定一个任务集
class My_task_set(TaskSet):
    host = 'http://82.156.74.26:9088'

    # 添加初始化方法
    def on_start(self):
        print("类似类中的构造方法，每个用户在任务开始前，只执行一次,在这里可以定义一个对象的属性，这样其它测试集就可以使用这个属性")

    def on_stop(self):
        print("类似类中的后置方法，每个用户在任务开始后，只执行一次,在这里可以定义一个对象的属性，这样其它测试集就可以使用这个属性")

    # 这是某个任务,30是比例，比如这里是30/50
    @task(30)
    def get_sku(self):
        # client就是个requests对象
        # catch_response，告诉locust如何判断请求失败还是成功
        res = self.client.get("/pinter/com/getSku?id=1", catch_response=True)
        if res.json == 200:
            res.success()
        else:
            res.failure("ff")
        print(res)

    @task(20)
    def get_login(self):
        data = {'userName': 'admin', 'password': 1234}
        # client就是个requests对象
        res = self.client.post("/pinter/com/login", data=data, catch_response=True)
        print(res)


class WebSite(HttpUser):
    # 被测系统的host（接口url）
    # host = 'http://82.156.74.26:9088'
    # 指定要执行哪个任务集
    # task_set = My_task_set
    # task_set = task(My_task_set)
    tasks = [My_task_set, ]

    # 请求和请求之间最小的间隔时间
    min_wait = 1000
    # 请求和请求之间最大的间隔时间
    max_wait = 2000

# Number of total users to simulate   模拟的用户数
# Spawn rate                          每秒钟产生的用户数
