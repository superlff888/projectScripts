# @Time  : 2022/01/20 21:16
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================






# 封装 ： 所有设计模式的基础;将相同特性性和行为动作封装成属性和方法


class AirPlane:
    name = ""
    color = ""

    def __set_name_(self, name):  # 私有化方法，加双横线
        self.name = name

    def set_color_(self, color):
        self.color = color
        print(f"设置的颜色为：{self.color}")


# 继承 ：（方法重写，调用子类自己的方法）
class CivilAirPlane(AirPlane):  # 民用飞机
    def save_person(self, num):
        print(f'民用机载人数量：{num}')


class JYAirPlane(AirPlane):  # 军用飞机
    pass


cap = CivilAirPlane()  # 括号一般不要省略
cap.set_color_("绿色")
AirPlane.set_color_(AirPlane(), "红色")  # 调用方法时，若类名不加括号，必须将实例"类名()"传进去

"""
# 多态
# 方法重写可以理解成一种多态的前提
"""


class Animal(object):
    def run(self):
        print('Animal is running...')

    def sleep(self):
        print("睡觉")


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run_a(self):
        print('Tortoise is running slowly...')


# a = list()  # a是list类型
# b = Animal()  # b是Animal类型
# c = Dog()  # c是Dog类型



"""
传哪个类的实例，就回调的响应类的方法
"""
def run_twice(animal):
    animal.run()
    animal.sleep()


run_twice(Tortoise())  # 注意：Tortoise()其实就是一个实例，t=Tortoise()只是将实例赋值于t

"""
总结：
1、继承的前提下 --> 方法重写
2、Dog、Cat、Tortoise三种动物分别有自己的run()方法,run_twice方法在没传入动物实例时，不知道调用的是哪种动物的run方法，只有传入某
   动物实例，才能明确调用谁的方法，这里注意 "类名()"其实就是实例，只是在写法习上习惯赋值于某一个简单的变量;
   要区别于"类名"不加括号，如果类名不加括号，在调用方法时，无法‘默认将实例赋予self’，必须将实例“类名()”传到方法中
"""

# 【拓展】
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
# 判断变量是不是属于该自定义类型，用isinstance()
isinstance(a, list)
isinstance(b, Animal)
print(isinstance(c, Dog))  # 返回True