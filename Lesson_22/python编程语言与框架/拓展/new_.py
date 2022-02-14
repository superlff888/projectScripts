# @Time  : 2021/05/06 19:54
# @Author    : House Lee
# -*-coding=utf-8-*-

"""
对象实例化的时候，第一个被调用的是  __new__方法




"""


class CapStr(str):
    # 第一个参数就是所需要创建的实例所属的类,参数在实例化时由python解释器自动识别
    def __new__(cls, string):  # 返回当前类的对象（当然也可以返回其他类的对象）当前类在init之前被调用；new方法中的参数会原封不动的传给init方法
        string = string.upper()
        print(super().isdigit("lee"))  # super()也可以调用父类方法
        return super().__new__(cls, string)  # str类型

    # def __init__(self, string):  # 验证该new方法中的参数会原封不动的传给init方法
    #     print("string=" + string)

    def eat(self, string):
        print(f"{string}爱你")


print(CapStr("i love you"))
a = CapStr("i love you")
