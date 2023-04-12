# -*- coding=utf-8 -*-
# @Time    : 2023/04/11 22:08
# @Author  : ╰☆H.俠ゞ
# =============================================================
# -*- coding=utf-8 -*-
# @Time    : 2022/09/03 14:24
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import sys
import webbrowser
from locust import HttpUser, task, TaskSet, between
sys.path.append(r'D:\Develop\git_pub_repositories\projectScripts\MStudent')
from TestFun_jiguang.__locust.参数化重复数据.get_csvDict import getCSVDict


class My_task_set(TaskSet):
    data_list = getCSVDict("/data.csv")

    def on_start(self):
        self.index = 0

    @task
    def login(self):
        url = '/pinter/com/login'
        data = My_task_set.data_list[self.index]
        self.index = (self.index+1) % len(My_task_set.data_list)  # 取模：循环使用csv文件数据
        with self.client.post(url=url, data=data, timeout=5, name='登录', catch_response=True) as res:
            if res.json()["message"] == 'success':
                res.success()
            else:
                res.failure(res.json())


class WebSite(HttpUser):
    # 被测系统的host（接口url）
    host = 'http://82.156.74.26:9088'
    tasks = [My_task_set, ]
    wait_time = between(1, 2)  # 单位：秒


# if __name__ == '__main__':
#     # 控制浏览器打开locust页面
#     webbrowser.open_new_tab('http://localhost:8089')
#     os.system("locust -f 参数化数据重复使用.py -u 10 -r 1 -t 1h20m5s --csv=result --stop-timeout=60 --master")
