# @Time  : 2022/02/15 10:10
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import os

# help(os)  # 查看对应模块(os)的帮助文档
print(dir(os))  # 查看对应模块(os)的属性和方法
import sys

"""可以处理文件和目录这些我们日常手动需要做的操作"""
"""操作系统相关"""
# # 1、获取系统名称
print(os.name)  # nt代码windows系统;posix代表linux
# # 2、获取系统环境变量
# print(f'environ:{os.environ}')
# # 3、获取指定的环境变量信息
# print(f"getenv: {os.getenv('PATH')}")  # 系统环境变量 PATH
#
# # 4、模拟Terminal终端命令
# os.system('cmd')  # linux
# """目录之‘增删改查’"""
# # 1、获取当前目录(目录不包含文件名，路径可以含文件名)
# print(f'获取当前目录: {os.getcwd()}')
# # 2、切换目录
# os.chdir('../sys_my/sys_import')
print(f'获取切换目录: {os.getcwd()}')  # 已经切到该目录下了 '../sys_my/sys_import'
# # 3、列出当前目录的所有文件
# print(os.listdir())  # f图标的时方法；v图标的是属性
# # 4、在当前目录下创建空目录 （目录已经切到'../sys_my/sys_import'，所以会在sys_import下新建一个空目录）
# # os.mkdir('mk_demo')  # 不能重复创建
# os.makedirs(r'mk_demo\1\2')  # 注意mkdir 不同于 makedirs
# print(r"已创建路径： mk_demo\1\2")
# # 5、重命名一个目录
# print(f'重命名前：{os.listdir()}')  # f图标的时方法；v图标的是属性
# os.rename('./mk_demo', 'mk')
# print(f'重命名后：{os.listdir()}')  # f图标的时方法；v图标的是属性
# # 6、删除空目录
# os.rmdir(r'mk\1\2')  # 删除文件夹2
# os.rmdir(r'mk\1')  # 删除文件夹1
# os.rmdir(r'mk')  # 删除文件夹mk_demo
# # 删除文件
# os.remove('./test.txt')  # 传入一个路径
#
#
# """路径相关"""
# # # 返回绝对路径
# print(f"当前文件的绝对路径 {os.path.abspath(r'./os_demo.py')}")
print(f"当前文件的abspath绝对路径 {os.path.abspath(__file__)}")
# # # 返回文件名
# # print(os.path.basename('./testDemo.py'))
#
# # 返回文件路径（不含文件名）
# print("返回文件路径（不含文件名）:")
print(os.path.dirname(r'D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest'))
print(os.path.dirname(r'D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\src\testDemo.py'))
print(os.path.basename(r'D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\src\testDemo.py'))
# print(f'返回文件路径 {os.path.dirname(os.path.abspath(__file__))}')
# print(f'返回文件base路径 {os.path.basename(os.path.abspath(__file__))}')

# print(os.path.abspath(__file__))
# # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# # print(f'导包路径: {sys.path}')

# # # 分割路径 （返回元组）
# print(os.path.split(r'D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\src\testDemo.py'))


"""
拼接路径  （该路径是模拟路径，属于字符串拼接)
D:\\Develop\\git_pub_repositories\\hogwartsCODE\\pythonBattle_pytest\\src\\../demo 表示先找src上级，定位上级下面的demo，其实是跟src平级
"""
print(os.path.join(os.path.dirname(r'D:\Develop\git_pub_repositories'),
                   os.path.dirname(__file__)))


# Path1 = 'home'
# Path2 = 'develop'
# Path3 = 'code'
#
# Path10 = Path1 + Path2 + Path3  # 字符串拼接(拼接成另外一个字符串)
# # join(a: AnyStr, *paths: AnyStr) -> AnyStr ; *paths为可变长参数
# Path20 = os.path.join(Path1, Path2, Path3)  # 路径拼接(用字符串参数拼接成路径)
# print('Path10 = ', Path10)
# print('Path20 = ', Path20)
#
# # 判断路径是否存在
# print(os.path.exists('./os_demo.py'))
