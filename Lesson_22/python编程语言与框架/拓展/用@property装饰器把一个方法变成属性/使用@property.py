# @Time  : 2022/01/26 11:08
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数；

"""


class Student(object):

    def set_score(self, value: int):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def get_score(self):
        return self._score


s = Student()
# s.set_score(9999)
s.set_score(60)
print(s.get_score())

"""
对任意的Student实例进行操作，就不能随心所欲地设置score了; 因此上面的调用方法又略显复杂，没有直接用属性这么直接简单
"""


# ==================================================================================================================
"""
既能检查参数，又可以用类似属性这样简单的方式来访问类的变量?
    答：Python内置的@property装饰器就是负责把一个方法变成属性调用的
"""


class Person:
    """
     birth方法：读写getter(getter)、setter；
     age方法：只读 @property(getter)
     """
    def __init__(self, name):
        self._birth = None
        self.name = name

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value: str) -> None:
        self._birth = value

    def eat(self):
        print(f"{self.name}已经{self.age}岁了,要控制饮食")  # p1.age ; p2.age

    @property
    def age(self):
        return 2022 - eval(self._birth)


p1 = Person('lee')
p2 = Person('john')
p3 = Person('lily')
print(f"{p3.name}的初始生日设置为：{p3._birth}")
p1.birth = '1991'
p2.birth = '1992'
birth_out1 = p1.birth
birth_out2 = p2.birth
print(birth_out1)  # '1991'
print(birth_out2)  # '1992'
p1.eat()
p2.eat()

