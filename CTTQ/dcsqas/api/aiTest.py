# -*- coding=utf-8 -*-
# @Time    : 2022/09/21 08:42
# @Author  : ╰☆H.俠ゞ
# =============================================================
import sys
from pprint import pprint
from time import sleep

from locust import HttpUser, TaskSet, task, events

sys.path.append(f"D:\\Develop\\git_pub_repositories\\projectScripts")  # （运行程序时）添加path环境变量
from CTTQ.dcsqas.web.Utils.tools import image_to_base64  # 添加环境变量后，才能找到CTTQ模块
from gevent._semaphore import Semaphore

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()


def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()  # 创建钩子方法(释放)
    sleep(1)
    print(f"虚拟用户总数:{n}")


# events.on_hatch_complete += on_hatch_complete
# 挂载到locust钩子函数（所有的Locust示例产生完成时触发）
events.spawning_complete.add_listener(on_hatch_complete)

n = 0


class AI_dcs(TaskSet):
    header = {
        "remoteuser": "AI",
        "token": "991a537f-2b2e-4e0b-a6af-d408308273d8",
        "Content-Type": "application/json;charset=UTF-8"
    }

    def initialize_user(self):
        global n
        n += 1
        print(f"初始化第{n}个用户")

    # 限制在所有用户准备完成前处于等待状态
    def on_start(self):
        self.initialize_user()  # 初始化用户(可使用locust设置用户个数)
        all_locusts_spawned.wait()  # 集合点，每个任务
        # print(f"虚拟用户总数{n}")

    # @task  # 任务==事务（单接口/多接口）
    def nlp_summary(self):
        base64_1, pre_b64_decode = image_to_base64(r'E:\CTTQ\项目\AI天晴门户\上传图片\身份证.png', 'base64', 'b64encode')
        # print(pre_b64_decode)
        json = {
            "imgName": "身份证.png",
            "side": "face",
            "imgBase64Code": pre_b64_decode
        }

        with self.client.post(url="/idCardNormalize/app/IDcard/normalized",
                              json=json, headers=self.header, catch_response=True) as response:
            try:
                if response.json()['msgCode'] == '700':
                    response.success()
                else:
                    response.failure("请求失败！")
            except Exception as e:
                print(f"response.text: {response.text}")
                print(f"response: {response}")
                print(f"response.content: {response.content}")
                print(f"response.status_code: {response.status_code}")
                print(f"response.raw: {response.raw}")
                raise e

        # # 用于demo
        # globals()["tmp"] = res.json()["code"]
        # assert globals()["tmp"] == 200

    @task
    # 获取全量资源
    def all_resource(self):
        with self.client.post(url="/resourceManage/all", headers=self.header, catch_response=True) as response:
            if response.json()['msgCode'] == "100":
                response.success()
            else:
                response.failure("请求失败！")

    @task
    # 请求部分资源
    def part_resource(self):
        payload = {
            "code": "gateAI",
        }
        with self.client.post(url="/resourceManage/code", params=payload, headers=self.header, catch_response=True) \
                as response:
            if response.json()['msgCode'] == "100":
                response.success()
            else:
                response.failure("请求失败！")

    # def demo(self):
    #     print(f"\n获得上一步的返回值:\n {globals()['tmp']}")  # 上一个方法执行完才能获得全局变量


class WebSite(HttpUser):
    # 指定要执行哪个任务集
    task_set = AI_dcs
    # task_set = task(My_task_set)
    tasks = [AI_dcs, ]
    # 请求和请求之间最小的间隔时间
    min_wait = 1000
    # 请求和请求之间最大的间隔时间
    max_waif = 2000
    # host = "https://dcsqas.cttq.com:6002"
    host = "http://172.17.6.116:6016"
