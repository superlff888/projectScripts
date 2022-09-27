# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 08:50
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
并发：多个任务同一 时间段 进行，即多线程【只有任务中存在sleep时，某个时间段空中才会存在多个苹果，也即是说多线程才能显现出来】
并行：多个任务同一时刻进行，即多进程

【需要加锁的场景】 "线程之间共享数据最大的危险在于多个线程同时修改一个变量 , 那就乱套了"!!!
GIL：GIL并不是Python的特性，Python完全可以不依赖于GIL，加锁是为了保证线程安全，比如需要保证不在数据库中重复取数；
    在我们的Python语言中多线程其实是假的多线程，它只会在一个CPU上运行，且在同一时刻只能有一个线程(只能启动一个线程)；
    在多核CPU(多个厕所)上，Python的多线程实际是串行执行的(运行时间段高度重合)，同一时刻多个线程并不会分布在多个CPU(举例：3个厕所)上运行

cpu：运行线程

举例：(1)任务添加等待时间，小丑扔苹果的过程就相当于多线程：扔出去一点(未完成)，第二个苹果就要扔出去
    (2) 扔苹果任务如果没有加等待时间，那么空中只会有一个苹果
轮循概念：线程一执行"一点"后就会去执行下一个线程；也就是说线程1还没执行完就去执行其他下线程，前提是函数任务中添加sleep时间
"""

# 因为线程属于同一个进程，因此它们之间共享内存区域，所以全局变量是公共的
import threading
import time
from copy import copy, deepcopy


def apple_1():
    print("苹果1")
    time.sleep(5)


def apple_2():
    print("苹果2")
    time.sleep(20)


def calc():
    a = 0
    while a != 9999*9999:
        a += 1


def calc_single():
    start_time = time.time()
    a = 0
    while a != 9999*9999*2:
        a += 1
    end_time = time.time()
    print(f"单线程运行时长为：{end_time - start_time}\n")


def main1():
    """
    【Thread类  常用参数】
    target 　　表示调用对象，即子线程要执行的任务
    name 　 子线程的名称
    args 　　 传入target函数中的位置参数,是一个元组，参数后必须加逗号隔开
    """
    # threading.Thread本质是创建线程
    thread1 = threading.Thread(target=apple_1)  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    thread2 = threading.Thread(target=apple_2)
    start_time = time.time()
    thread1.start()  # 启动线程，start方法就是去帮你调用run方法
    thread2.start()
    end_time = time.time()
    # # 理解为：当扔苹果1和苹果2的时候，禁止扔主线程苹果
    # thread1.join()  # 让其他线程等待thread1自己执行完成
    # thread2.join()  # 让其他线程等待thread2自己执行完成
    # 多个任务同一时间段进行，即并发
    print(f"运行时长为：{end_time-start_time}\n")  # 打印时间后，线程依旧在跑，说明这两个线程运行时间段高度重合

    print("有多少小丑？", threading.active_count())  # 返回当前活动的 Thread 对象的数量
    print("这些小丑是谁？", threading.enumerate())  # 返回当前活动的所有线程对象的列表


def main2():
    thread1 = threading.Thread(target=calc)  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    thread2 = threading.Thread(target=calc)
    start_time = time.time()
    thread1.start()  # 启动线程，start方法就是去帮你调用run方法
    thread2.start()
    thread1.join()  # 让其他线程等待thread1自己执行完成
    thread2.join()
    end_time = time.time()
    print(f"多线程计算运行时长为：{end_time-start_time}\n")


if __name__ == '__main__':
    main1()
    # main2()  # 多线程计算，线程间本质就是在排队
    # calc_single()  # 单线程计算
