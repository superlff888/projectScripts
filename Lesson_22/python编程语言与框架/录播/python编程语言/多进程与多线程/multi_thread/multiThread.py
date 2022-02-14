# @Time  : 2022/01/25 21:31
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import os
import threading
import time


"""
线程轮循执行，即上一个线程还没结束，下一个线程就开始执行了
"""

#
# def task():
#     time.sleep(5)


# 主线程与子线程轮循被执行，计算时间的代码【end_time - start_time】不会等两个子线程执行完，也不会在两个等5秒思考时间sleep(5),
# 在开始执行线程那一刻，计算时间的代码就开始被执行了，这就是轮循的意思，例如小丑耍苹果
# def main():  # 主线程
#     start_time = time.time()  # 当前时间（current time），即线程开始时间
#     thread1 = threading.Thread(target=task)  # 子线程1
#     thread2 = threading.Thread(target=task)  # 子线程2
#     thread1.start()
#     thread2.start()
#     end_time = time.time()  # 当前时间（current time），即线程结束时间
#     print(end_time - start_time)  #
#
#
# if __name__ == '__main__':
#     main()


# ==========================================================================================================
print("=====================================================================================================")
# ==========================================================================================================

"""
加join()的作用：前面线程执行结束，后面的线程才能被执行
"""


def task(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))  # os.getpid()获取进程id
    time.sleep(5)


def main():  # 主线程
    start_time = time.time()  # 当前时间（current time），即线程开始时间
    thread1 = threading.Thread(target=task, args=('test1',))  # 子线程1
    thread2 = threading.Thread(target=task, args=('test2',))  # 子线程2
    # 两个子线程执行结束前，禁止执行其他线程
    thread1.start()
    thread2.start()
    thread1.join()  # 可以等待子进程1结束后再继续往下运行
    thread2.join()  # 可以等待子进程2结束后再继续往下运行
    end_time = time.time()  # 当前时间（current time），即线程结束时间
    print(end_time - start_time)  #


if __name__ == '__main__':
    main()