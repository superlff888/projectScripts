# -*- coding=utf-8 -*-
# @Time    : 2023/04/12 01:19
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import queue
import webbrowser

from gevent._semaphore import Semaphore
from locust import events, TaskSet, HttpUser, task, between, FastHttpUser

from MStudent.TestFun_jiguang.__locust.集合点.get_csvDict import getCSVDict

all_locusts_spawned = Semaphore()  # 信号量，内置的计数器
all_locusts_spawned.acquire()  # 获取信号量

def on_hatch_complete(**kwargs):  # hook函数
    all_locusts_spawned.release()  # 释放信号量


events.spawning_complete.add_listener(on_hatch_complete)  # 事件监听库


n = 0
class UserBehavior(TaskSet):
    def login_(self):
        global n
        n += 1
        print(f"{n}个虚拟用户开始启动，并登录")

    def on_start(self):
        self.login_()  # 每个用户先完成登录，在集合点等着
        self.queue_data = WebSite.queue_data  # 不同用户，从队列中获得的消息不同，所以要做self实例成员化（10个用户并发登录）
        all_locusts_spawned.wait()  # 等待信号量

    @task
    def login(self):
        url = '/pinter/com/login'
        try:

            data = self.queue_data.get_nowait()  # 从队列中获取消息(账号和密码)赋值给data
            print(data)
            with self.client.post(url=url, data=data, timeout=5, name='登录', catch_response=True) as res:
                if res.json()["message"] == 'success':
                    res.success()
                else:
                    res.failure(res.json())
        except queue.Empty:
            print("数据为空了...")
            exit()


class WebSite(FastHttpUser):

    queue_data = queue.Queue()  # 实例化一个队列
    for dic in getCSVDict("/data.csv"):
        queue_data.put_nowait(dic)  # 将item消息写入队列
    # 被测系统的host（接口url）
    host = 'http://82.156.74.26:9088'
    tasks = [UserBehavior, ]
    wait_time = between(1, 2)  # 单位：秒


if __name__ == '__main__':
    # 控制浏览器打开locust页面
    webbrowser.open_new_tab('http://localhost:8089')
    os.system("locust -f 集合点.py -u 10 -r 1 -t 1h20m5s --csv=result --stop-timeout=60")
