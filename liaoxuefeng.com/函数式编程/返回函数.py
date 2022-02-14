# @Time  : 2021/05/20 16:38
# @Author    : House Lee
# -*-coding=utf-8-*-
"""
闭包
"""


def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)  # 函数f没有被立即执行，只是将函数的内存地址追加到列表中
    return fs  # return的i为最后取到的3


print(f'\n遍历出三个函数的内存地址列表为：{count1()}')
f1, f2, f3 = count1()  # 解包
print("-----------------------------------\n三个函数加上括号，分别去运行")
print(f1())
print(f2())
print(f3())
print("三个函数运行结束-----------------------------------")


def count2():
    fs = []
    for i in range(1, 4):
        def f(i):
            return i * i
        fs.append(f(i))
    return fs


f1, f2, f3 = count2()
print(f'每个i都被遍历到了，所以返回的是三个函数的运行结果，所以列表及其元素为：{count2()}')


def count3():
    def f(j):
        def g():
            return j * j

        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


d1, d2, d3 = count3()
print(f'\n因为结果被遍历出来，所以三个函数的执行结果为：{d1()}, {d2()}, {d3()}')


# 可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum() -> int:
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum  # 此处返回sum的话，即是返回sum函数的内存地址；sum()返回的即是该函数执行结果


# print(lazy_sum(1, 3, 5, 7, 9))

# f1 = lazy_sum(1, 3, 5, 7, 9)
# print(f1)  # 打印的是内存地址
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f2)
# print(f1 == f2)


# 关键是：返回的函数并没有立刻执行，而是直到调用了f()才执行，取得是变量i*i的最终结果
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
# print(count()())
print(f1())
print(f2())
print(f3())


#  返回函数不要引用任何循环变量，或者后续会发生变化的变量

#  说白点，返回函数外面不能有任何循环变量
