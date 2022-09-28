def init(self, name):
    self.name = name


def eat(self):
    print("i am eating...")


# Animal = type("Animal", (object,), {"__init__": init, "eat": eat})
Animal = type("Animal", (object,), dict(__init__=init, eat=eat))
a1 = Animal("sc1")
a1.eat()
print(a1.name)

"""
使用元类
"""


class MyMate(type):
    def __new__(mcs, name, bases, attrs):
        print(f"mcs:  {mcs}")
        if "ufo" not in attrs:
            raise TypeError("必须设置ufo属性")
        return type.__new__(mcs, name, bases, attrs)


class A(metaclass=MyMate):
    ufo = "sc"


print(A)

d3 = {"a": 3, "b": 6, "c": 1}
print(d3.get("a"))
d3.update({"a": 5, "b": 8, "c": 2, "d": 9})
print(d3)
for key in d3:
    print(key)

dict_a = {}
print(type(dict_a))




