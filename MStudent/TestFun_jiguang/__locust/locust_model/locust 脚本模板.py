# -*- coding=utf-8 -*-
# @Time    : 2022/09/03 15:48
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import webbrowser

from locust import HttpUser, TaskSet, task


# pytest
class UserBehave(TaskSet):

    # 启动locust是setup
    def setup(self):
        print("task setup")

    # 停止locust是teardown
    def teardown(self):
        print("task teardown")

    # 虚拟用户启动时运行
    def on_start(self):
        print("start")
        print("类似类中的构造方法，每个用户在任务开始前，只执行一次,在这里可以定义一个对象的属性，这样其它测试集就可以使用这个属性")

    # 虚拟用户结束时运行
    def on_stop(self):
        print("stop")
        print("类似类中的后置方法，每个用户在任务开始后，只执行一次,在这里可以定义一个对象的属性，这样其它测试集就可以使用这个属性")

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
    tasks = [UserBehave, ]
    # task_set = task(UserBehave)
    # task_set = UserBehave


if __name__ == '__main__':
    # 控制浏览器打开locust页面
    webbrowser.open_new_tab('http://localhost:8089')
    # 控制cmd执行locust，“MyTaskSet.py”为需要运行py脚本名字，“http://82.156.74.26:9088”为压测服务器地址; --headless 后台执行,无web界面
    # -u 用户数 -r 每秒启动用户数  -t 运行时间  --csv 测试结果保存在csv文件中  --stop-timeout=60  停止延迟时间(防止突然停止，造成请求错误)
    os.system("locust -f MyTaskSet.py,demo1.py,demo2.py -u 2 -r 1 -t 1h30m20s --csv=result --stop-timeout=60")
