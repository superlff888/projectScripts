# -*- coding=utf-8 -*-
# @Time    : 2022/10/16 20:26
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""

"""
import functools


class Log:
    def __init__(self):
        pass

    @staticmethod
    def log(text):  # 装饰器函数需要带参数的时候，需要装饰器函数入参处接收参数,本质就是定义函数参数
        def decorator(func):  # 一定要在装饰器函数体内接收被装饰的原函数
            # @functools.wraps(func)
            def wrapper(*args, **kw):
                print(f'\n3、装饰器参数为：{text}; 原函数为：{func.__name__}')
                print(f"4、返回并再调用返回的被装饰原始函数func，即{func()}")  # 被装饰函数一般会在装饰器函数中执行，因为装饰器本身就是为了加强被装饰函数
                print(f"args为：{args}")
                print(f"{text}在内嵌函数wrapper中打印")
                def Called():
                    print("又套一层Called内嵌函数")
                    def inner():
                        print("inner是最里层函数")
                    return inner
                return Called  # 根据业务return想要的"对象"，也可以返回func
            # print(f"{text}在内嵌函数decorator打印")
            print(f"\n2、返回并执行{func.__name__}")
            return wrapper
        print(f"{text}在log函数体内打印")
        print(f"\n1、执行调用log('execute')后，返回函数{decorator.__name__}")
        return decorator


# class called:
#     @staticmethod
#     def other_log():
#         print("我被链式调用了")  # pytest.mark.parametrize中pytest.mark本质是一个对象，可以调用装饰器函数parametrize()


@Log.log("text")
def now():
    print('\n5、date is 2015-3-25')


isWrapper = now()  # 为啥可以传入参数2？看总结就明白了，wrapper(*args, **kw)可接收任意参数
print(isWrapper)  # <function Log.log.<locals>.decorator.<locals>.wrapper.<locals>.Called at 0x00000233FCE59550>
isWrapper()()


"""
【总结】装饰器特性:
1、核心：[装饰器特性]被装饰函数可被自动传给装饰器函数“入参位置”或函数体; 被装饰函数被认为是装饰器函数的实参。
   注意：(1) [函数的参数化处理]被装饰函数是作为实参，既可以放到装饰器函数入参处，也可以放到装饰器函数体中;
        (2) 第一层内嵌函数被认为是装饰器函数体,被装饰函数只能被第一层嵌套函数以实参的形式自动接收一次;
2、被装饰函数只能被装饰器函数自动传递一次。
   “装饰器函数体”由于装饰器特性会自动接收“被装饰函数”这个参数，然后返回“下一层嵌套函数”(即wrapper())并自动执行。被装饰函数不会以参数形式二次传递给
   下一层内嵌函数；但是自被装饰函数传进装饰器函数后，也就是从接收被装饰函数的函数或函数体开始，里面每一层的内层函数体内可以使用被装饰函数，相当于函数基
   础学习时，在函数体中运行实参。
    now()  # 打印print(now)的结果： <function Log.log.<locals>.decorator.<locals>.wrapper.<locals>.Called at 0x000001D53BD99550>
3、被装饰函数一般会在装饰器函数中执行，因为装饰器本身就是为了加强被装饰函数。
3、本质就是函数的参数处理+被装饰函数以实参形式自动传递给装饰器函数。

"""