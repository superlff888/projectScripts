# @Time  : 2022/01/19 22:58
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
全局变量（模块） ！= 类变量（类共有属性） ！= 成员变量（self.param） ！= 局部变量（方法的入参）
"""


class Person:
    """
    先定义变量类型
    """
    # 类变量：类中定义的变量,需要用类名调用 “Person.name”；类共有的属性;
    can_cry = "Yes"  # 会哭
    name = "default"

    def __init__(self, name, age, gender, weigh):
        print("init function")
        self.name = name
        self.age = age
        self.gender = gender
        self.weigh = weigh

    def set__(self, name, age, gender, weigh):
        self.name = name
        self.age = age
        self.gender = gender
        self.weigh = weigh

    @classmethod  # 类方法；运用场景：不想实例化一个对象
    def eat(cls):  # cls替代了self
        print(f'{cls.name}正在吃汉堡')

    def play(self):
        print(f'打球的那个{self.gender}生应该不超过{self.age}岁')

    def jump(self):
        print(f'他有{self.weigh}，怎么可能跳高')


p = Person("le", 21, "男", "70kg")
print(Person.can_cry)  # 一般情况下，类属性用类去调用，例如吃狗粮
print(p.name)
p.set__("lee", 26, "男", "75kg")  # p.name = "lee"; self为实例本身，谁调就是谁

"""
x = 10
def a(arg):
    print(arg)
a(x)  #  调用函数a
"""
p.eat()  # @classmethod装饰成类方法，实例对象调用类方法时，属性name取值类变量值
p.play()  # 实例对象p在调用play方法时，默认将实例p传给该方法的play位置
p.jump()
Person.eat()  # @classmethod装饰成类方法后，属性name取值类变量值
Person.jump(p)  # 不是用实例对象调用的实例方法，所以没有默认将实例传给方法的self位置，因而要传递实例进去
