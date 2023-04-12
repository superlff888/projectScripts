# -*- coding=utf-8 -*-
# @Time    : 2023/04/11 23:08
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import queue
import webbrowser
from locust import HttpUser, between, TaskSet, task
from TestFun_jiguang.__locust.参数化数据不重复使用.get_csvDict import getCSVDict


class My_task_set(TaskSet):

    def on_start(self):
        self.queue_data = WebSite.queue_data

    @task
    def login(self):
        url = '/pinter/com/login'
        try:
            data = self.queue_data.get_nowait()  # 从队列中取出user赋值给user_data
            print(data)
            with self.client.post(url=url, data=data, timeout=5, name='登录', catch_response=True) as res:
                if res.json()["message"] == 'success':
                    res.success()
                else:
                    res.failure(res.json())
        except queue.Empty:
            print("数据为空了...")
            exit()


class WebSite(HttpUser):
    """模拟3个用户并发注册九个账号，要求注册账号不重复，注册完毕后结束测试"""
    queue_data = queue.Queue()  # 实例化一个队列
    for dic in getCSVDict("/data.csv"):
        queue_data.put_nowait(dic)  # 将item消息写入队列
    # 被测系统的host（接口url）
    host = 'http://82.156.74.26:9088'
    tasks = [My_task_set, ]
    wait_time = between(1, 2)  # 单位：秒


if __name__ == '__main__':
    # 控制浏览器打开locust页面
    webbrowser.open_new_tab('http://localhost:8089')
    os.system("locust -f 不重复使用.py -u 10 -r 1 -t 1h20m5s --csv=result --stop-timeout=60")
