# @Time  : 2022/01/20 22:23
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
【装饰器】
1、不用实例化、都可以直接调用
2、提升代码的可读性
3、装饰器：类方法classmethod、静态方法staticmethod
"""


"""
【类方法】
定义：
1、使用 @classmethod 装饰器，第一个参数为类本身，所以通常使用cls命名做区分(非强制)
2、在类内可以直接使用类方法或类变量，无法直接使用实例变量或方法
调用：
无需实例化，直接通过 类.方法名 调用，也可以通过 实例.方法名 调用
"""


class classMethod:
    """
    self 不等于 cls ，实例本身 不同于类本身
    """
    CLASS_PARAM = 0

    def __init__(self):
        self.a = '123'

    @classmethod  # 类方法
    def class_method_1(cls):
        # cls.demo_method_1()  # 类方法内cls不能直接调用实例方法（需要传参数self?）
        # cls.a  # 也不能直接调用实例属性 AttributeError: type object 'classMethod' has no attribute 'a'
        cls.class_method_2()  # 类方法中类本身cls可以调用类方法
        print("这是一个类方法1", cls.CLASS_PARAM)  # 类本身cls可以调用类属性

    def demo_method(self):
        print("这是一个普通方法")

    @classmethod  # 类方法
    def class_method_2(cls):
        print("这是一个类方法2")


classMethod.class_method_1()

demo = classMethod()
demo.class_method_1()  # 实例对象可以调用类方法
demo.demo_method()  # 实例对象可以可调用普通方法


"""
【静态方法】
定义：
1、使用 @staticmethod 装饰器，没有和类本身有关的参数（去掉self）
2、无法直接使用任何类变量、类方法或者实例方法、实例变量
调用：
无需实例化，直接通过 类.方法名 调用，也可以通过 实例.方法名 调用
"""


# 1. 定义
class MethodsDemo:
    param_a = 0

    @staticmethod
    def static_demo(param1):  # 没有self和cls,即不需要自动传入实例本身； 但是可以正常传参
        """
        静态方法
        :return:
        """
        print("静态方法", param1)  # 无法直接调用类变量


# 2. 调用
M = MethodsDemo()
MethodsDemo.static_demo("a")  # 通过类名调用
M.static_demo("b")  # 通过实例调用


"""
类方法实例案例
1、右边的代码实现的需求是格式化输出时间
2、如果现在需求变更：传入的参数 ”年、月、日” 没法保证格式统一，可能是json，可能是其他格式的字符串，在不修改构造函数的前提下，如何更改代码
"""


class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"

    @classmethod
    def json_format_class(cls):
        year2, month2, day2 = json_data1["year"], json_data1["month"], json_data1["day"],
        print("\n通过类方法json_format_class处理后：")
        return cls(year2, month2, day2)  # 类本身(year2, month2, day2)


# 方法1：
def json_format_1(json_data1):
    year1, month1, day1 = json_data1["year"], json_data1["month"], json_data1["day"],
    return year1, month1, day1


demo = DateFormat(2017, 7, 1)
print(demo.out_date())

# 方法1
json_data1 = {"year": 2022, "month": 2, "day": 16}
print(json_format_1(json_data1))  # 返回一个元组 (2022, 2, 16)
year, month, day = json_format_1(json_data1)  # 解包
demo = DateFormat(year, month, day)
print(demo.out_date())  # 输入的时间为2022年，2月，16日

# 方法2
# DateFormat.json_format_class()返回的是 cls(year2, month2, day2)，然后调用方法cls().out_date()
DateFormat.json_format_class().out_date()  # 相当于DateFormat().out_date()


"""
1、此方法没有任何和实例、类相关的部分，可以作为一个独立函数使用，某些场景下，从业务逻辑来说又属于类的一部分 
例子：简单工厂方法
"""


# static 使用场景
class Jinx(object):
    pass


def EZ():
    pass


class Timo(object):
    pass


class HeroFactory:
    # staticmethod 使用场景，
    # 方法所有涉及到的逻辑都没有使用实例方法或者实例变量的时候
    # 伪代码
    @staticmethod
    def create_hero(hero):
        if hero == "ez":
            return EZ()
        elif hero == "jinx":
            return Jinx()
        elif hero == "timo":
            return Timo()
        else:
            raise Exception("此英雄不在英雄工厂当中")

