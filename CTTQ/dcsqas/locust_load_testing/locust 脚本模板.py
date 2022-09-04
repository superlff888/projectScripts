# -*- coding=utf-8 -*-
# @Time    : 2022/09/03 15:48
# @Author  : ╰☆H.俠ゞ
# =============================================================


from locust import HttpUser, TaskSet, task


# pytest
class UserBehave(TaskSet):

    # 启动locusts是setup
    def setup(self):
        print("task setup")

    # 停止locust是teardown
    def teardown(self):
        print("task teardown")

    # 虚拟用户启动时运行
    def on_start(self):
        print("start")

    # 虚拟用户结束时运行
    def on_stop(self):
        print("stop")

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def info(self):
        self.client.get("/info")


class WebSiteUser(HttpUser):
    def setup(self):
        print("locust setup")

    def teardown(self):
        print("locust teardown")

    # 类似于 between(3, 5) ,指的是：每个用户执行两个任务的间隔时间
    min_wait = 3000  # 单位 毫秒
    max_wait = 5000  # 默认1000毫秒

    # 被测系统的host（接口url）
    host = '*.*.*.*:port'

    # 指定要执行哪个任务集
    tasks = [UserBehave]
    # task_set = task(UserBehave)
    # task_set = UserBehave
