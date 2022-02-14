# @Time  : 2021/05/27 11:35
# @Author    : House Lee
# -*-coding=utf-8-*-
"""

# multiprocessing模块提供了一个Process类来代表一个进程对象
# os.getpid()：Return the current process id.

"""
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name1: str):
    print(f'Run child process {name1} at ({os.getpid()})...')


# 子进程要执行的代码
def run_proc2(name2: str):
    print(f'Run child process2 {name2} at ({os.getpid()})...')
    return os.getpid()


'''
# tuple_a = ('a',)
# print(type(tuple_a))  # <class 'tuple'>
'''
if __name__ == '__main__':
    print(f'Parent process {os.getpid()}.')
    # 创建一个进程对象（子进程），即将定义的方法作为参数传进去
    p = Process(target=run_proc, args=('test',))  # args=('test') 表示的是字符串，而不是元组
    p2 = Process(target=run_proc2, args=('dev',))  # args=('dev') 表示的是字符串，而不是元组
    print('Child process will start.')
    p.start()  # 启动子进程
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p2.start()  # 启动子进程
    p2.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print(f'Child process end.')


# ==============================================================================================================
