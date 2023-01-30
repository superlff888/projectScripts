# @Time  : 2022/01/19 08:32
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================


list_a = [1, 2, 3]
a, b, c = list_a  # 解包，分别赋值给三个变量


def f(x, y, z):
    print(x, y, z)


f(a, b, c)
f(*list_a)  # 作为实参：传参时，*用于解包


def f1(x, y, *z):  # 函数的形参中，装包到可变长参数中
    print(x, y, z)


f1(1, 2, 3, 4, 56, 8)  # 优先分配给‘不可变参数’


def func(x, y, z, w):
    print(x, y, z, w)


kwarg = {"x": 1, "y": 2, "z": 3, "w": 4}  # 注意：变量名要一致；因为解包后分别做了赋值，变为 x=1,y=2,z=3,w=4

func(**kwarg)  # 解包后，作为实参传给函数


def func1(**kwargs):  # 作为形参时，**装包的作用,把所有默认参数装包到kwargs
    print(kwargs.get('a'))


func1(a=1, b=2)
